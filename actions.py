from concurrent.futures import ThreadPoolExecutor as thread_pool_executor

from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as web_driver_wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup as beautiful_soup

import random
import helper
import config

def until(driver, what, timeout=config.driver_timeout):
    return web_driver_wait(driver, timeout).until(what)

def find_cakes(driver, thread):
    def _check_newest_cakes(page_src):
        soup = beautiful_soup(page_src, 'html.parser')
        found = set()

        # check if cake day
        # this is pretty crap bc it re-searches the thread over and over
        # ideally it should only search subelements of the 'more replies' button
        for cake in soup.select('svg[id*="cakeday"]'):
            username = cake.parent.select('a[href*="/user/"]')

            try:
                found.add(username[0].get_text())
            except:
                raise
                
                # the community cake day will trigger this, ignore it
                # pass

        return found

    # the main thread uses Selenium to expand the thread fully
    # a second thread searches for all users who have a cake day

    try:
        driver.get(thread)
    except WebDriverException as e:
        helper.thread_safe_print(f'skipping thread because connection was refused on {thread}')

        return set()

    helper.thread_safe_print(f'searching thread "{helper.truncate(driver.title, 75)}" for cakes')

    cakes = set()

    with thread_pool_executor() as executor:
        future = executor.submit(_check_newest_cakes, driver.page_source)

        while True:            
            try:
                helper.js_scroll(driver)
                
                # click any 'more reply' buttons that have loaded
                # if no more load, timeout                
                elems_to_open = until(driver, helper.any_elements_clickable(
                    (by.XPATH, "//*[contains(@id, 'moreComments')]//*[contains(text(), 'more repl')]")))
                
                for e in elems_to_open:
                    helper.js_click_elem(driver, e)
            
            except StaleElementReferenceException as stale_except:
                pass
            
            except TimeoutException as timeout_except:

                # .result() will wait for the thread to finish searching
                cakes.update(future.result())
                break

            # once the search thread finishes, re-launch it
            if future.done():
                cakes.update(future.result())

                future = executor.submit(_check_newest_cakes, driver.page_source)
    
    return cakes

def wish_user_cakeday(driver, user):    
    driver.get(f'http://www.reddit.com/user/{user}/comments/')

    serviced_ids = set()

    # find all reply buttons
    try:
        reply_buttons = until(driver, helper.any_elements_clickable((by.XPATH, "//button[text()='Reply']")))
    except TimeoutException:
        return False # re-queue this user
    
    for reply_button in reply_buttons:
        if len(serviced_ids) >= config.user_post_limit:
            break

        try:
            post_id_elem = reply_button.find_element_by_xpath(".//ancestor::*[contains(@class,'Comment')]")
            post_date_elem = post_id_elem.find_element_by_xpath("..//descendant::a[contains(@id,'Created')]")
            post_reply_elem = post_id_elem.find_element_by_xpath(".//button[text()='Reply']")
        except StaleElementReferenceException:
            return False # re-queue this user

        # extract info
        post_id = post_id_elem.get_attribute('class')[8:]
        post_date = post_date_elem.text

        # check that the date lines up
        if post_id not in serviced_ids and ('minute' in post_date or 'hour' in post_date):
            helper.thread_safe_print(f'replying to post "{post_id}" made {post_date} by user {user}')
            
            try:
                # reply to post
                helper.js_click_elem(driver, post_reply_elem)

                reply_box = until(driver, ec.element_to_be_clickable(
                    (by.CSS_SELECTOR, 'div[contenteditable="true"]')), config.reply_timeout)

                helper.js_scroll_to(driver, reply_box)
                helper.js_click_elem(driver, reply_box)
                
                reply_box.send_keys(random.choice(config.phrases))

                if config.safe_mode:
                    reply_box.send_keys(keys.CONTROL + 'a')
                    reply_box.send_keys(keys.BACKSPACE)

                submit_box = until(driver, ec.element_to_be_clickable((by.CSS_SELECTOR, 'button[type="submit"]')))
                
                helper.js_click_elem(driver, submit_box)

                # test if it has submitted by waiting until reply box disappears
                if until(driver, ec.staleness_of(reply_box), config.reply_timeout):
                    driver.back()
                    
            except TimeoutException:
                helper.thread_safe_print('reply timed out, passing')

                driver.back()
                
            else:
                serviced_ids.add(post_id)

        try:
            helper.js_scroll(driver, '150')

        # will not scroll if alert is present
        # cringe but necessary
        except UnexpectedAlertPresentException:
            try:
                driver.switch_to_alert().accept()
            except:
                pass

    return True

def scrape_thread(driver, community):
    driver.get(f'http://www.reddit.com/r/{community}/')

    posts = set()

    while len(posts) < config.thread_scrape_limit:
        try:
            for post in until(driver, helper.any_elements_clickable((by.XPATH, "//*[contains(@class, 'scrollerItem')]"))):
                if 'promotedlink' in post.get_attribute('class'):
                    continue
                if 'Blank' in post.get_attribute('class'):
                    continue
                if len(post.find_elements_by_xpath('.//*[contains(@class, "sticky")]')):
                    continue
                
                posts.add(post.find_element_by_css_selector('[data-click-id="comments"]').get_attribute('href'))
                                
            helper.js_scroll(driver)
        
        except TimeoutException as timeout_except:
            helper.thread_safe_print('timeout')
            break

    return posts

def login(driver):
    driver.get('https://www.reddit.com/login')

    username = driver.find_element_by_css_selector('input[name="username"]')
    password = driver.find_element_by_css_selector('input[name="password"]')

    username.clear()
    username.send_keys(config.username)
    password.clear()
    password.send_keys(config.password)
    password.send_keys(keys.RETURN)

    # wait for login to succeed
    try:
        until(driver, ec.title_contains('front page of the internet'))
    except:
        assert 'login failed'
        driver.quit()

def make_driver():
    driver = None

    if config.browser == 'chrome':
        _chrome_options = chrome_options()

        _chrome_options.add_argument("--disable-extensions")
        _chrome_options.add_argument("--disable-gpu")
        _chrome_options.add_argument("--disable-notifications")
        _chrome_options.add_argument("--disable-logging")
        _chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        _chrome_options.add_experimental_option('prefs', {
            'prefs': {'intl.accept_languages': 'en,en-US'},
            'profile.default_content_setting_values.notifications' : 2})

        #_chrome_options.add_argument(f"user-data-dir={config.chrome_profile_path}")

        if config.headless:
            _chrome_options.add_argument("--start-maximized")
            _chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=_chrome_options)
    elif config.browser == 'firefox':
        _firefox_profile = FirefoxProfile(config.firefox_profile_path)
        _firefox_options = firefox_options()

        _firefox_options.headless = config.headless
        
        driver = webdriver.Firefox(_firefox_profile, options=_firefox_options)
    else:
        raise Exception(f'unknown brower "{config.browser}"')

    if not config.skip_login:
        login(driver)

    return driver
