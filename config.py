headless = False
browser = 'chrome'
skip_login = False
safe_mode = False

driver_timeout = 5
reply_timeout = 12
user_post_limit = 1
thread_scrape_limit = 15
thread_queue_limit = 30

finder_thread_count = 1 # the number of drivers dedicated to finding new threads
reply_thread_count = 2 # the number of drivers dedicated to replying to users
search_thread_count = 3 # the number of drivers dedicated to searching a post for cake days

# make sure your feed settings are:
# adult content on
# safe browsing mode off
# community themes off
username = 'username'
password = 'password'

# warning: chrome profile does not work
chrome_profile_path = r'.\config\chrome_user_data'
firefox_profile_path = r'.\config\firefox_user_data'
users_file = r'.\config\users.pickle'

phrases = [
    'Happy cake day!',
    'Happy cake day my friend!',
    'I am here to humbly wish you a happy cake day!',
    'Happy cake day kind internet stranger!',
    'Just dropping in to say: happy cake day!']

subreddits = [
        'all',
        'aww',
        'videos',
        'Jokes',
        'ThatsInsane',
        'dataisbeautiful',
        'Damnthatsinteresting',
        'iamverybadass',
        'tifu',
        'SelfAwarewolves',
        'MaliciousCompliance',
        'bestof',
        'Music',
        'WhitePeopleTwitter',
        'instant_regret',
        'dankmemes',
        'teenagers',
        'changemyview',
        'iamatotalpieceofshit',
        'perfectlycutscreams',
        'cringepics',
        'harrypotter',
        'RoastMe',
        'sadcringe',
        'photoshopbattles',
        'AskAnAmerican',
        'FragileWhiteRedditor',
        'ShittyLifeProTips',
        'MadeMeSmile',
        'TooAfraidToAsk',
        'woodworking',
        'OutOfTheLoop',
        'AskMen',
        'MemeEconomy',
        'BeAmazed',
        'fakehistoryporn',
        'entertainment',
        'nextfuckinglevel',
        'me_irl',
        'australia']
