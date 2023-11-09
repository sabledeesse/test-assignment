from client import Session
from urllib.parse import urljoin
import time
from time import sleep

USER_ID = "user23"
URL = "https://petstore.swagger.io/v2/user/"
ORDER_ID = 9

s = Session()


def create_new_user():
    # Тест на добавление нового пользователя
    print("--------------------------------------------")
    print("\n Test for creating new user \n")

    user_json = {
        "id": 1,
        "username": USER_ID,
        "firstName": "Vera",
        "lastName": "Pirojomba",
        "email": "email@nomail.com",
        "password": "12345",
        "phone": "+70000000000",
        "userStatus": 0,
    }
    ok_json = {"code": 200, "type": "unknown", "message": "1"}
    response = s.post(URL, json=user_json)
    assert response.status_code == 200
    assert response.json() == ok_json
    if response.status_code == 200:
        print(f'User {USER_ID} added:', response.json())
        print("Status code is ", response.status_code)
        return user_json
    else:
        print("Error retrieving data:", response.text)


def get_new_user(new_user: str):
    # Тест на поиск нового пользователя
    print("--------------------------------------------")
    print("\n Test for getting new user \n")
    response = s.get(urljoin(URL, USER_ID))
    assert response.status_code == 200
    assert response.json() == new_user
    if response.status_code == 200:
        data = response.json()
        print(f'User {USER_ID} added:', data)
        print("Status code is ", response.status_code)
    else:
        print("Error retrieving data:", response.text)


def log_in_new_user():
    # Тест на логин нового пользователя
    print("--------------------------------------------")
    print("\n Test for logging in new user \n")

    response = s.get(URL + "login", auth=("user23", "12345"))

    time_stamp = round(time.time() * 1000)
    ok_json = {"code": 200, "type": "unknown", "message": ("logged in user session:" + str(time_stamp))}
    assert response.status_code == 200

    for x in response.json():
        assert x == x in ok_json

    for key in ok_json:
        item = response.json().get(key)
        if key != "message":
            assert item == ok_json[key]
        else:
            assert isinstance(item, str) is True
            splitted = item.split(":")
            assert len(splitted) == 2

            info_resp, ts_resp = splitted
            info_ok, ts_ok = ok_json[key].split(":")

            assert info_resp == info_ok

            assert abs(int(ts_resp) - int(ts_ok)) < 5 * 1000

    if response.status_code == 200:
        print(f'User {USER_ID} is logged in:', response.json())
        print("Status code is ", response.status_code)
    else:
        print("Error retrieving data:", response.text)


def log_out_new_user():
    # Тест на разлогин нового пользователя
    print("--------------------------------------------")
    print("\n Test for logging out new user \n")
    ok_json = {"code": 200, "type": "unknown", "message": "ok"}
    response = s.get(URL + "logout")
    assert response.status_code == 200
    assert response.json() == ok_json
    if response.status_code == 200:
        print(f'User {USER_ID} is logged out:', response.json())
        print("Status code is ", response.status_code)
    else:
        print("Error retrieving data:", response.text)


def delete_new_user():
    # Тест на удаление нового пользователя
    print("--------------------------------------------")
    print("\n Test for deleting new user \n")
    ok_json = {"code": 200, "type": "unknown", "message": USER_ID}
    response = s.delete(urljoin(URL, USER_ID))
    assert response.status_code == 200
    assert response.json() == ok_json

    if response.status_code == 200:
        data = response.json()
        print(f'User {USER_ID} deleted:', data)
        print("Status code is ", response.status_code)
    else:
        print("Error retrieving data:", response.text)


def get_deleted_user():
    # Тест на удаление нового пользователя
    print("--------------------------------------------")
    print("\n Test for getting deleted user \n")
    ok_json = {"code": 1, "message": "User not found", "type": "error"}
    response = s.get(urljoin(URL, USER_ID))
    assert response.status_code == 404
    assert response.json() == ok_json
    if response.status_code == 404:
        data = response.json()
        print(f'User {USER_ID} not found:', data)
        print("Status code is ", response.status_code)
    else:
        print("Error retrieving data:", response.text)


def delete_deleted_user():
    # Тест на удаление удаленного пользователя
    print("--------------------------------------------")
    print("\n Test for deleting deleted user \n")

    response = s.delete(urljoin(URL, USER_ID))
    assert response.status_code == 404

    if response.status_code == 404:
        print(f'User {USER_ID} not found:')
        print("Status code is ", response.status_code)
    else:
        print("Error retrieving data:", response.text)


def tests():
    new_user = create_new_user()
    sleep(0.3)
    get_new_user(new_user=new_user)
    sleep(0.1)
    log_in_new_user()
    sleep(0.1)
    log_out_new_user()
    sleep(0.5)
    delete_new_user()
    sleep(0.1)
    get_deleted_user()
    sleep(0.1)
    delete_deleted_user()
