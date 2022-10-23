from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import pandas as pd
import logging

# Creating a log file for documentation
logging.basicConfig(filename="message_log.log", level=logging.INFO, format="%(asctime)s %(message)s")

try:
    # Setting up the driver
    driver = webdriver.Chrome(executable_path=r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe")
    # Entering the website through the driver
    driver.get("https://www.demoblaze.com/")

    # Waiting - because the driver works faster than the loading time of the browser, it is necessary to wait for the website to load
    driver.implicitly_wait(10)

    # Login button search
    driver.find_element(By.LINK_TEXT, "Log in").click()
    # Entering the username and password in the appropriate places
    driver.find_element(By.ID, 'loginusername').send_keys('anonymous number one')
    driver.find_element(By.ID, 'loginpassword').send_keys('20220914')
    # Login
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    # Waiting for the page to load
    time.sleep(5)

    # Nexus 6 product search
    element = driver.find_element(By.LINK_TEXT, 'Nexus 6')
    # Checking if the product found is Nexus 6
    assert element.text == 'Nexus 6', 'The name is not worth it Nexus 6'
    # Checking if the ID of the found product is equal to 3, according to the link to which the product refers
    link = element.get_attribute('href')
    assert link[-1] == '3', 'No find was found whose ID is equal to 3'
    # Enter the product details
    element.click()

    # Waiting for the page to load
    time.sleep(5)

    # Checking if the product entered is a Nexus 6
    assert driver.find_element(By.XPATH, '//h2[@class="name"]').text == 'Nexus 6', 'The name is not worth it Nexus 6'
    # Adding the product to the cart
    driver.find_element(By.LINK_TEXT, 'Add to cart').click()
    # Beyond the cart
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    # Waiting for the page to load
    time.sleep(5)

    # Creating a dataframe from a list of products in the cart
    table = pd.read_html(driver.page_source)[0]

    # Checking if there is one or more products in the cart
    assert len(table) == 1, 'More than one item'
    # Checking if the price of the product in the cart is 650
    assert table['Price'][0] == 650, 'The price is not worth 650'
    # Checking if the name of the product in the cart is a Nexus 6
    assert table['Title'][0] == 'Nexus 6', 'The name is not worth it Nexus 6'

    # Logging success When the program was successful
    logging.info("Success, the program is working as expected")

except AssertionError as msg:
    # Logging an error when tests fail
    logging.error(msg)
except NoSuchElementException:
    # Logging critical when the elements are not found
    logging.critical('The element was not found')
