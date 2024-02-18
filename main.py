import requests
import pytest

# post
def create_user():
    data = {
        "name": "test",
        "job": "user123"
    }

    response = requests.post('https://reqres.in/api/users', json=data).json()
    print(response)


def get_users():
    response = requests.get('https://reqres.in/api/users?page=2').json()
    print(response)


def get_user():
    response = requests.get('https://reqres.in/api/users/3').json()
    print(response)


def get_user():
    response = requests.get('https://reqres.in/api/users/3').json()
    print(response)


def get_wrong_user():
    response = requests.get('https://reqres.in/api/users/23').json()  # 404
    print(response)


def get_list_resource():
    response = requests.get('https://reqres.in/api/unknown').json()
    print(response)


def get_single_resource():
    response = requests.get('https://reqres.in/api/unknown/3').json()
    print(response)


# put
def update_user():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put('https://reqres.in/api/users/3', data=data).json()
    print(response)


# patch
def update_user():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put('https://reqres.in/api/users/3', data=data).json()
    print(response)


# delete
def delete_user(): #получаем 204 код
    response = requests.delete('https://reqres.in/api/users/2')
    print(response)

delete_user()
# post
def register_user():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post('https://reqres.in/api/register', data=data).json()
    print(response)

def bad_register_user():
    data = {
        "email": "sydney@fife"
    }
    response = requests.post('https://reqres.in/api/register', data=data).json()
    print(response)


def login_user():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post('https://reqres.in/api/login', data=data).json()
    print(response)


def bad_login_user():
    data = {
        "email": "eve.holt@reqres.in",
    }
    response = requests.post('https://reqres.in/api/login', data=data).json()
    print(response)

