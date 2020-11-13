headless = True
browser = 'chrome'
skip_login = False
safe_mode = False

driver_timeout = 5
reply_timeout = 12
user_post_limit = 1
thread_scrape_limit = 15
search_thread_count = 4 # the number of drivers dedicated to searching a post for cake days

username = 'username'
password = 'password'

# warning: chrome profile does not work
chrome_profile_path = r'.\config\chrome_user_data'
firefox_profile_path = r'.\config\firefox_user_data'
users_file = r'.\config\users.pickle'
#chrome_profile_path = r'C:\Users\camer\Documents\Programming\Python\karma_farmer\config\chrome_user_data'
#firefox_profile_path = r'C:\Users\camer\Documents\Programming\Python\karma_farmer\config\firefox_user_data'
#users_file = r'C:\Users\camer\Documents\Programming\Python\karma_farmer\config\users.pickle'

phrases = ['Happy cake day!']

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
