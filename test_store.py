from test_pets import (add_new_pet)
from urllib.parse import urljoin
from client import Session
import json
from time import sleep

PET_ID = 202308
URL = 'https://petstore.swagger.io/v2/store/order/'
ORDER_ID = 10

s = Session()


def purchase_new_pet():
    #Тест на покупку нового питомца
    print('--------------------------------------------')
    print('\n Test for buying new pet \n')

    data_from_api = {
        "id": 10,
        "petId": 202308,
        "quantity": 1,
        "shipDate": "2023-11-09T00:28:30.705Z",
        "status": "placed",
        "complete": True
    }
    ok_response = {
        "id": 10,
        "petId": 202308,
        "quantity": 1,
        "shipDate": "2023-11-09T00:28:30.705+0000",
        "status": "placed",
        "complete": True
    }
    response = s.post(URL, json=data_from_api)
    assert response.status_code == 200
    assert response.json() == ok_response
    if response.status_code == 200:
        data = response.json()
        print('Pet {PET_ID} purchased:', data)
        print('Status code is ', response.status_code)
    else:
        print('Error retrieving data:', response.text)


def find_order():
    #Тест на поиск нового заказа по id
    print('--------------------------------------------')
    print('\n Test for finding new order \n')
    ok_response = {
        "id": 10,
        "petId": 202308,
        "quantity": 1,
        "shipDate": "2023-11-09T00:28:30.705+0000",
        "status": "placed",
        "complete": True
    }
    response = s.get(urljoin(URL, str(ORDER_ID)))
    assert response.status_code == 200
    assert response.json() == ok_response
    if response.status_code == 200:
        data = response.json()
        print('Order {ORDER_ID} placed:', data)
        print('Status code is ', response.status_code)
    else:
        print('Error retrieving data:', response.text)


def delete_order():
    #Тест на удаление нового заказа по id
    print('--------------------------------------------')
    print('\n Test for deleting new order \n')
    ok_json = {
        "code": 200,
        "type": "unknown",
        "message": "10"
    }
    response = s.delete(urljoin(URL, str(ORDER_ID)))
    assert response.status_code == 200
    assert response.json() == ok_json
    if response.status_code == 200:
        data = response.json()
        print('Order {ORDER_ID} deleted:', data)
        print('Status code is ', response.status_code)
    else:
        print('Error retrieving data:', response.text)


def delete_non_existent_order():
    #Тест на удаление несуществующего заказа по id
    print('--------------------------------------------')
    print('\n Test for deleting none-exist order \n')

    ok_json = {
        "code": 404,
        "type": "unknown",
        "message": "Order Not Found"
    }
    response = s.delete(urljoin(URL,  str(ORDER_ID)))
    assert response.status_code == 404
    assert response.json() == ok_json
    if response.status_code == 404:
        data = response.json()
        print('Order {ORDER_ID} not found:', data)
        print('Status code is ', response.status_code)
    else:
        print('Error retrieving data:', response.text)


def find_non_existent_order():
    #Тест на поиск несуществующего заказа по id
    print('--------------------------------------------')
    print('\n Test for finding non-existent order \n')

    ok_json = {
        "code": 1,
        "type": "error",
        "message": "Order not found"
    }
    response = s.get(urljoin(URL,  str(ORDER_ID)))
    assert response.status_code == 404
    assert response.json() == ok_json
    if response.status_code == 404:
        data = response.json()
        print('Order {ORDER_ID} not found:', data)
        print('Status code is ', response.status_code)
    else:
        print('Error retrieving data:', response.text)


def tests():
    new_pet = add_new_pet()
    purchase_new_pet()
    find_order()
    delete_order()
    delete_non_existent_order()
    find_non_existent_order()

