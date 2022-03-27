import json
import pickle
from datetime import datetime
import requests
from API_Client import *
from ChallengeCodeGenerator import *
from dotenv import load_dotenv
from os import getenv, path

load_dotenv()
APP_CLIENT_ID = getenv('APP_CLIENT_ID')
APP_CLIENT_SECRET = getenv('APP_CLIENT_SECRET')
USER_DATA_PATH = './userData'
CHALLENGE_CODE = None


def generate_authorization_link() -> str:
    global CHALLENGE_CODE
    CHALLENGE_CODE = get_new_code_verifier()
    return f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={APP_CLIENT_ID}&code_challenge={CHALLENGE_CODE}'


def generate_new_user_token(auth_code: str, user_id: int):
    url = 'https://myanimelist.net/v1/oauth2/token'
    data = {
        'client_id': APP_CLIENT_ID,
        'client_secret': APP_CLIENT_SECRET,
        'code': auth_code,
        'code_verifier': CHALLENGE_CODE,
        'grant_type': 'authorization_code'
    }
    response = requests.post(url, data)
    response.raise_for_status()
    token = response.json()
    response.close()
    date_now = datetime.now()
    timestamp = date_now.timestamp()
    token['timestamp'] = int(round(timestamp))
    save_user_data(user_id, token)


def renew_user_token(user_token: dict) -> dict:
    url = 'https://myanimelist.net/v1/oauth2/token'
    data = {
        'client_id': APP_CLIENT_ID,
        'client_secret': APP_CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': user_token['refresh_token']
    }
    response = requests.post(url, data)
    response.raise_for_status()
    token = response.json()
    response.close()
    date_now = datetime.now()
    timestamp = date_now.timestamp()
    token['timestamp'] = int(round(timestamp))
    return token


def check_user_auth(user_id: int):
    user_data = load_user_data()
    if user_id in user_data.keys():
        return True
    else:
        return False


def save_user_data(user_id: int, token: dict):
    user_data = load_user_data()
    user_data[user_id] = token
    with open('userData', 'wb', buffering=0) as file:
        pickle.dump(user_data, file)


def load_user_data() -> dict:
    if path.exists(USER_DATA_PATH):
        with open('userData', 'rb') as file:
            user_data = pickle.load(file)
        return user_data
    else:
        return dict()


print(load_user_data())


# print(link)
# link = 'https://api.myanimelist.net/v2/anime?q=attack on titan'
# # link = 'https://api.myanimelist.net/v2/users/@me'
# #link = 'https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&limit=117'
# # #link = 'https://api.myanimelist.net/v2/anime/39783?fields=my_list_status'
# token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjAwNTExY2Y1MTc3ZTI4NGEzNGFlNWQ1ZGFmYzhhMDgwYzNkMmMxMTNiMjNkOGI5NzQzYmE3MzRhMGQ3YjY1N2ZkMTk4YjY2OThhOWY0NjM1In0.eyJhdWQiOiI5NGI4Y2RhMDkyNjExMTA5OWZkMDc5MTI2ZWU0OTdlNyIsImp0aSI6IjAwNTExY2Y1MTc3ZTI4NGEzNGFlNWQ1ZGFmYzhhMDgwYzNkMmMxMTNiMjNkOGI5NzQzYmE3MzRhMGQ3YjY1N2ZkMTk4YjY2OThhOWY0NjM1IiwiaWF0IjoxNjQ1Nzc1MTIzLCJuYmYiOjE2NDU3NzUxMjMsImV4cCI6MTY0ODE5MDcyMywic3ViIjoiMTA5NDQzOTIiLCJzY29wZXMiOltdfQ.O3lj0wPMD5JRB7TDNjkkPbGr2F5kncPAitH8tRDzYRUF3oCah_LXqMSfxsrAVuqEGaguXoO-Sf-RFIXhKuo0myOgYcLko-aF2SEFisCIBLqYZN5JA35I9wGL8OM4xjxE_Ad0z3arCWxQIsgNxklhCFdoOubofZVf86KhJRbrCZ0ww78B7-yss2LKNqOBH84wvDnQ1HOC1ylAZ4XFbpvb_sHtYjWEN-_gIOzsSpijiWK_lwyrS-dW4Kz6il8W5Ab1UGzLS6f3_VoQ322rEmDBrKruykvzQj_GlGIH0ozXc2JDZpLRvnzwNaYDGgqA3ro4AYXBfYS-4n4X0RDdqiX1Ug'
# request = requests.get(link, headers={'Authorization': f'Bearer {token}'})
# respond = request.json()
# print(respond.keys())
# print(json.dumps(respond, indent=True))

# anime_id = 39783
# data = {
#     "status": 'watching',
#     "score": 10,
#     "num_watched_episodes": 12
# }
# response = requests.put(UPDATE_ALIST.format(anime_id), data=data,
#                         headers={'Authentication': f'Bearer {token}'})
# response.raise_for_status()
# print(response.json())
#YA EBAL V ROT ETI PV. 2.5k strok ebanutiy chel