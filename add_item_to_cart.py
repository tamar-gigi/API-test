# דרך ראשונה
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import pandas as pd
import logging

# Creating a log file for documentation
logging.basicConfig(filename="message_log.log", level=logging.INFO, format="%(asctime)s %(message)s")
id_item = '3'
message_id = 'No find was found whose ID is equal to 3'
name_item = 'Nexus 6'
message_name = 'The name is not worth it Nexus 6'
price_item = 650
message_price = 'The price is not worth 650'
message_count = 'More than one item'
user_name = 'anonymous number one'
password = '20220914'


def login():
    # Login button search
    driver.find_element(By.LINK_TEXT, "Log in").click()
    # Entering the username and password in the appropriate places
    driver.find_element(By.ID, 'loginusername').send_keys(user_name)
    driver.find_element(By.ID, 'loginpassword').send_keys(password)
    # Login
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    # Waiting for the page to load
    time.sleep(5)


def add_nexus():
    # Nexus 6 product search
    element = driver.find_element(By.LINK_TEXT, name_item)
    # Checking if the product found is Nexus 6
    assert element.text == name_item, message_name
    # Checking if the ID of the found product is equal to 3, according to the link to which the product refers
    link = element.get_attribute('href')
    assert link[-1] == id_item, message_id
    # Enter the product details
    element.click()

    # Waiting for the page to load
    time.sleep(5)

    # Checking if the product entered is a Nexus 6
    assert driver.find_element(By.XPATH, '//h2[@class="name"]').text == name_item, message_name
    # Adding the product to the cart
    driver.find_element(By.LINK_TEXT, 'Add to cart').click()


def move_cart():
    # Beyond the cart
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    # Waiting for the page to load
    time.sleep(5)


def validate():
    # Creating a dataframe from a list of products in the cart
    table = pd.read_html(driver.page_source)[0]

    # Checking if there is one or more products in the cart
    assert len(table) == 1, message_count
    # Checking if the price of the product in the cart is 650
    assert table['Price'][0] == price_item, message_price
    # Checking if the name of the product in the cart is a Nexus 6
    assert table['Title'][0] == name_item, message_name


try:
    # Setting up the driver
    driver = webdriver.Chrome(executable_path=r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe")
    # Entering the website through the driver
    driver.get("https://www.demoblaze.com/")

    # Waiting - because the driver works faster than the loading time of the browser, it is necessary to wait for the website to load
    driver.implicitly_wait(10)

    login()

    add_nexus()

    move_cart()

    validate()

    # Logging success When the program was successful
    logging.info("Success, the program is working as expected")

except AssertionError as msg:
    # Logging an error when tests fail
    logging.error(msg)
except NoSuchElementException:
    # Logging critical when the elements are not found
    logging.critical('The element was not found')
