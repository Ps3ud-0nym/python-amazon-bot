#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

driver_location = "/usr/bin/chromedriver"
binary_location =  "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location
options.page_load_strategy = 'eager'

login_url = 'https://amazon.co.uk/signin'

def purchase(username,password,item_url):
    driver = webdriver.Chrome(executable_path=driver_location)
    wait = WebDriverWait(driver, 10)

    driver.get(login_url)

    driver.find_element_by_xpath(
        '//input[@id="ap_email"]').send_keys(username) 
    driver.find_element_by_xpath(
        '//input[@id="continue"]').click()

    driver.find_element_by_xpath(
        '//input[@id="ap_password"]').send_keys(password) 
    driver.find_element_by_xpath(
        '//input[@id="signInSubmit"]').click()

    wait.until(
        presence_of_element_located((By.XPATH, '//div[@id="pageContent"]')))

    driver.get(item_url)

    while not  driver.find_element_by_xpath('//div[@id="newAccordionRow"]//div[@role="radio"]//div[2]//div[1]'):
        driver.refresh()

    driver.find_element_by_xpath(
        '//div[@id="newAccordionRow"]//div[@role="radio"]//div[2]//div[1]').click()

    driver.find_element_by_xpath(
        '//input[@id="add-to-cart-button"]').click()

    driver.find_element_by_xpath(
        '//a[@id="hlb-ptc-btn-native"]').click()

    driver.find_element_by_xpath(
        '//input[@aria-labelledby="submitOrderButtonId-announce"]').click()

purchase('test@test.com','Password','https://amazon.co.uk/gp/product/item1')
