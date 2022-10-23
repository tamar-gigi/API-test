from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pandas

try:
    driver = webdriver.Chrome(executable_path=r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe")
    wait = WebDriverWait(driver, 500)
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.find_element("link text", "Log in").click()
    driver.find_element(By.ID, 'loginusername').send_keys('anonymous number one')
    driver.find_element(By.ID, 'loginpassword').send_keys('20220914')
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    time.sleep(5)

    element = driver.find_element(By.LINK_TEXT, 'Nexus 6')
    link = element.get_attribute('href')
    assert link[-1] == '3', 'No find was found whose ID is equal to 3'
    element.click()
    driver.find_element(By.LINK_TEXT, 'Add to cart').click()
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    time.sleep(5)

    table = pandas.read_html(driver.page_source)[0]

    assert len(table) == 1, 'More than one item'
    assert table['Price'][0] == 650, 'The price is not worth 650'
    assert table['Title'][0] == 'Nexus 6', 'The name is not worth it Nexus 6'
    print('Succeeded!!!!!!!!!!')

except AssertionError as msg:
    print(msg)
except NoSuchElementException:
    print('The element was not found')
