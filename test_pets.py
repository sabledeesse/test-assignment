from time import sleep
from client import Session
from urllib.parse import urljoin

PET_ID = 202308
URL = 'https://petstore.swagger.io/v2/pet/'
s = Session()
def adding_new_pet() -> str:
    #Тест на добавление нового питомца
    print('\n Test for adding new pet \n')
    pet = {
        "id": PET_ID,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "frog in a car",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "pending"
    }
    response = s.post(URL, json=pet)

    assert response.status_code == 200
    if response.status_code == 200:
        data = response.json()
        print('Pet {PET_ID} added successfully:', data)
        print('Status code is ', response.status_code)
        return data
    else:
        print('Error retrieving data:', response.text)


def getting_new_pet(new_pet: str):

    #Тест на получение добавленного питомца
    print('--------------------------------------------')
    print('\n Test for getting new pet \n')

    #URL = 'https://petstore.swagger.io/v2/pet/{}'.format(PET_ID)
    ok_json = new_pet
    response = s.get(urljoin(URL, str(PET_ID)))

    assert response.status_code == 200
    assert response.json() == ok_json
    if response.status_code == 200:
        data = response.json()
        print('Pet {PET_ID} found:', data)
        print('Status code is ', response.status_code)
    else:
        print('Error retrieving data:', response.text)


def deleting_new_pet():
    #Тест на удаление добавленного питомца
    print('--------------------------------------------')
    print('\n Test for deleting new pet \n')

    ok_json = {'code': 200, 'type': 'unknown', 'message': str(PET_ID)}

    response = s.delete(urljoin(URL, str(PET_ID)))

    assert response.status_code == 200
    assert response.json() == ok_json
    if response.status_code == 200:
        data = response.json()
        print('Pet {PET_ID} deleted:', data)
        print('Status code is ', response.status_code)
    else:
        print('Error retrieving data:', response.text)


def searching_deleted_pet():
    #Тест на поиск удаленного питомца
    print('--------------------------------------------')
    print('\n Test for searching deleted pet \n')

    ok_json = {'code': 1, 'type': 'error', 'message': 'Pet not found'}
    response = s.get(urljoin(URL, str(PET_ID)))
    assert response.status_code == 404
    assert response.json() == ok_json
    if response.status_code == 404:
        print('Pet {PET_ID} not found')
        print('Status code is', response.status_code)
    else:
        print('Error retrieving data:', response.text)

def deleating_deleted_pet():
    #Тест на удаление удаленного питомца
    print('--------------------------------------------')
    print('\n Test for adding new pet \n')
    response = s.delete(urljoin(URL, str(PET_ID)))
    assert response.status_code == 404
    if response.status_code == 404:
        print('Pet {PET_ID} not found')
        print('Status code is', response.status_code)
    else:
        print('Error retrieving data:', response.text)


def tests():
    new_pet = adding_new_pet()
    getting_new_pet(new_pet=new_pet)
    deleting_new_pet()
    searching_deleted_pet()
    deleating_deleted_pet()
