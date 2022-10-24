# דרך שניה
import requests
import base64
import logging

# Creating a log file for documentation
logging.basicConfig(filename="message_log_2.log", level=logging.INFO, format="%(asctime)s %(message)s")

# Setting Variables
API_URL = "https://api.demoblaze.com/"
user_name = 'anonymous number one'
password = '20220914'
item = "prod.html?idp_=3"
cart = 'cart.html/'
id_item = '3'
message_id = 'No find was found whose ID is equal to 3'
name_item = 'Nexus 6'
message_name = 'The name is not worth it Nexus 6'
price_item = 650
message_price = 'The price is not worth 650'
message_count = 'More than one item'


def Login():
    # Converting the password to BASE64
    b64_password = base64.b64encode(bytes(password, 'utf-8')).decode('utf-8')
    # Creating an object to send when logging in that consists of a username and password
    login = {"username": user_name, "password": b64_password}
    # Calling a server and receiving the token
    token1 = requests.post(API_URL+'login', json=login, verify=False)
    return token1


def Add_to_cart(cookie):
    # Creating an add-to-cart object that consists of an ID (actually generated randomly each time by the GUID function, I couldn't create it), the token, a flag, and a product ID
    add = {"id": "0cbfca6b-2029-91cb-28c8-ba14333e252c", "cookie": cookie.text, "prod_id": str(item[-1]), "flag": True}
    # Adding the product to the basket
    requests.post(API_URL+'addtocart', json=add, verify=False)


def move_to_cart(cookie):
    # Pass to the cart by the fixer and flag
    view = {"cookie": cookie.json().split(":")[-1][1:], "flag": True}
    obj = requests.post(API_URL+'viewcart', json=view, verify=False)
    return obj


def check(items_cart):
    # Checking if there is more than one item
    assert len(items_cart) == 1, message_count

    # Receiving data about the items in the cart by ID
    id1 = {"id": items_cart[0]["prod_id"]}
    obj = requests.post(API_URL + 'view', json=id1, verify=False)

    # Checking if the identifier ID =3
    assert str(obj.json()['id']) == id_item, message_id
    # Checking if the price is worth 650
    assert int(obj.json()['price']) == price_item, message_price
    # Checking if the name of the product is Nexus 6
    assert str(obj.json()['title']) == name_item, message_name


try:
    token = Login()

    Add_to_cart(token)

    items = move_to_cart(token)
    items = items.json()["Items"]

    check(items)

    logging.info("Success, the program is working as expected")

except AssertionError as msg:
    logging.error(msg)