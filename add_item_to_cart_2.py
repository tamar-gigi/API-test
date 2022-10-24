import requests
import base64
import logging

logging.basicConfig(filename="message_log_2.log", level=logging.INFO, format="%(asctime)s %(message)s")

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
    b64_password = base64.b64encode(bytes(password, 'utf-8')).decode('utf-8')
    login = {"username": user_name, "password": b64_password}
    token1 = requests.post(API_URL+'login', json=login, verify=False)
    return token1


def Add_to_cart(cookie):
    add = {"id": "0cbfca6b-2029-91cb-28c8-ba14333e252c", "cookie": cookie.text, "prod_id": str(item[-1]), "flag": True}
    requests.post(API_URL+'addtocart', json=add, verify=False)


def move_to_cart(cookie):
    view = {"cookie": cookie.json().split(":")[-1][1:], "flag": True}
    obj = requests.post(API_URL+'viewcart', json=view, verify=False)
    return obj


def check(items_cart):
    assert len(items_cart) == 1, message_count

    id1 = {"id": items_cart[0]["prod_id"]}
    obj = requests.post(API_URL + 'view', json=id1, verify=False)

    assert str(obj.json()['id']) == id_item, message_id
    assert int(obj.json()['price']) == price_item, message_price
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