import pathlib

headless = True
browser = 'chrome'
skip_login = False
safe_mode = False
use_proxy = True

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

# chrome profile doesn't work
chrome_profile_path = pathlib.Path('profile').absolute()
firefox_profile_path = r'.\config\firefox_user_data'
users_file = r'.\config\users.pickle'

chrome_driver=r'drivers\chromedriver.exe'

proxy_list = [
    ("103.226.105.102", "5678", "socks4"),
    ("111.90.181.6", "5678", "socks4"),
    ("103.193.39.160", "5678", "socks4"),
    ("173.244.200.154", "62679", "socks4"),
    ("103.9.55.177", "5678", "socks4"),
    ("103.226.105.102","5678","socks4"),
    ("103.246.103.159","5678","socks4"),
    ("118.127.125.34","5678","socks4"),
    ("202.178.125.65","5678","socks4")]

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
