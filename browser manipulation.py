# using selenium to open browser/input information
from selenium import webdriver
browser = webdriver.Chrome('C:\\Users\monroem\PycharmProjects\chromedriver.exe')
type(browser)
browser.get('https://www.facebook.com/')
email = browser.find_element_by_id('email')
email.send_keys('notreal@yahoo.com')
email.submit()


