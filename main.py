from concurrent.futures import ThreadPoolExecutor as thread_pool_executor
from concurrent.futures import wait
from threading import Lock as lock

from queue import Queue as queue

import actions
import traceback
import config
import helper

def thread_worker(thread_queue):
    driver = actions.make_driver()
    
    for subreddit in config.subreddits:
        helper.thread_safe_print(f'scraping r/{subreddit}')
        
        for t in actions.scrape_thread(driver, subreddit):
            thread_queue.put(t, block=True)
            
    helper.thread_safe_print('exhausted the list of communities to look for threads')

    driver.quit()

def user_worker(thread_queue, user_queue):
    driver = actions.make_driver()
    
    while True:
        thread = thread_queue.get(block=True)

        for user in actions.find_cakes(driver, thread):
            helper.thread_safe_print(f'adding user "{user}" to the queue')
            
            user_queue.put(user, block=True)

def reply_worker(user_queue, done_set, done_lock):
    driver = actions.make_driver()

    while True:
        user = user_queue.get(block=True)

        done_lock.acquire()
        not_contained = user not in done_set
        done_lock.release()
        
        if no_contained:    
            if actions.wish_user_cakeday(driver, user):
                done_lock.acquire()
                done_set.add(user)
                helper.write_db(config.users_file, done_set)
                done_lock.release()
                
            else:
                helper.thread_safe_print(f'messaging user "{user}" failed, re-queueing')
                
                user_queue.put(user, block=True)
        
if __name__ == '__main__':
    thread_queue = queue() # threads to be searched
    user_queue = queue() # users with a cakeday to spam 
    done_set = set() # users who have already been wished a happy cake day
    done_lock = lock() # lock to prevent race conditions when accessing done_set

    try:
        done_set = helper.read_db(config.users_file)

        helper.thread_safe_print(f'loaded {len(done_set)} users from db')
            
    except EOFError:
        helper.thread_safe_print('db was empty, creating new')
        
    with thread_pool_executor() as executor:
        futures = []

        futures.extend([executor.submit(thread_worker, thread_queue) for _ in range(config.finder_thread_count)])
        futures.extend([executor.submit(user_worker, thread_queue, user_queue) for _ in range(config.search_thread_count)])
        futures.extend([executor.submit(reply_worker, user_queue, done_set, done_lock) for _ in range(config.reply_thread_count)])

        not_done = futures

        try:
            while len(not_done):
                done, not_done = wait(not_done, timeout=0)

                # rethrow any exceptions raised by the futures
                for f in done:
                    f.result()

        except Exception as e:
            helper.thread_safe_print(f'an exception occured: {e}')
            helper.thread_safe_print(traceback.format_exc())
            
            for f in not_done:
                f.cancel()

            wait(not_done, timeout=None)

            raise e
