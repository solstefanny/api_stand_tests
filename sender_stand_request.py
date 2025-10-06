import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=body,
                        headers=data.headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + "/api/db/resources/user_model.csv")

