from threading import current_thread

import pickle

def thread_safe_print(x):
    print(f'[T{current_thread().ident}]: {str(x)}\n', end='')

def truncate(x, length):
    return x[:length] + (x[length:] and "..")

def js_click_elem(driver, e):
    driver.execute_script("arguments[0].click();", e)

def js_scroll(driver, by='document.body.scrollHeight || document.documentElement.scrollHeight'):
    driver.execute_script(f'window.scrollBy(0,{by});')

def js_scroll_to(driver, element):
    driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)

def any_elements_clickable(locator):
    def _predicate(driver):
        return [element for element in driver.find_elements(*locator)]
    
    return _predicate

def read_db(file):
    with open(file, 'rb') as db:
        return pickle.load(db)

def write_db(file, data):
    with open(file, 'wb') as db:
        pickle.dump(data, db)
