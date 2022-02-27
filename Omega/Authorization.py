import json
from datetime import datetime
import requests
from API_Client import *
from ChallengeCodeGenerator import *


APP_CLIENT_ID = '94b8cda0926111099fd079126ee497e7'
APP_CLIENT_SECRET = '8ada8a9ff8547c2cb156a790af7741b93f074c8c6beaef5364047dbd3d82f5d5'
CHALLENGE_CODE = CODE_VERIFIER = None


def generate_authorization_link():
    global CHALLENGE_CODE, CODE_VERIFIER
    CHALLENGE_CODE = CODE_VERIFIER = get_new_code_verifier()
    return f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={APP_CLIENT_ID}&code_challenge={CHALLENGE_CODE}'


def generate_new_user_token(auth_code: str) -> dict:
    url = 'https://myanimelist.net/v1/oauth2/token'
    data = {
        'client_id': APP_CLIENT_ID,
        'client_secret': APP_CLIENT_SECRET,
        'code': auth_code,
        'code_verifier': CODE_VERIFIER,
        'grant_type': 'authorization_code'
    }
    response = requests.post(url, data)
    response.raise_for_status()
    token = response.json()
    response.close()
    date_now = datetime.now()
    timestamp = date_now.timestamp()
    token['timestamp'] = int(round(timestamp))
    return token


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


def authorize():
    auth_link = generate_authorization_link()
    print(auth_link)
    auth_code = input('Enter auth code: ')
    new_token = generate_new_user_token(auth_code)
    response = requests.get(MAL_USER_INFO, headers={'Authorization': f'Bearer {new_token["access_token"]}'})
    response.raise_for_status()
    nickname = response.json()['name']
    return nickname, new_token

# print(generate_authorization_link())
# code = input('Auth')
# toen = generate_new_user_token(code)
# print(toen)
# link = ANIME.format('39783')
# print(link)
link = 'https://api.jikan.moe/v4/users/I1yStery'
# link = 'https://api.myanimelist.net/v2/users/@me'
# #link = 'https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&limit=117'
# #link = 'https://api.myanimelist.net/v2/anime/39783?fields=my_list_status'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjAwNTExY2Y1MTc3ZTI4NGEzNGFlNWQ1ZGFmYzhhMDgwYzNkMmMxMTNiMjNkOGI5NzQzYmE3MzRhMGQ3YjY1N2ZkMTk4YjY2OThhOWY0NjM1In0.eyJhdWQiOiI5NGI4Y2RhMDkyNjExMTA5OWZkMDc5MTI2ZWU0OTdlNyIsImp0aSI6IjAwNTExY2Y1MTc3ZTI4NGEzNGFlNWQ1ZGFmYzhhMDgwYzNkMmMxMTNiMjNkOGI5NzQzYmE3MzRhMGQ3YjY1N2ZkMTk4YjY2OThhOWY0NjM1IiwiaWF0IjoxNjQ1Nzc1MTIzLCJuYmYiOjE2NDU3NzUxMjMsImV4cCI6MTY0ODE5MDcyMywic3ViIjoiMTA5NDQzOTIiLCJzY29wZXMiOltdfQ.O3lj0wPMD5JRB7TDNjkkPbGr2F5kncPAitH8tRDzYRUF3oCah_LXqMSfxsrAVuqEGaguXoO-Sf-RFIXhKuo0myOgYcLko-aF2SEFisCIBLqYZN5JA35I9wGL8OM4xjxE_Ad0z3arCWxQIsgNxklhCFdoOubofZVf86KhJRbrCZ0ww78B7-yss2LKNqOBH84wvDnQ1HOC1ylAZ4XFbpvb_sHtYjWEN-_gIOzsSpijiWK_lwyrS-dW4Kz6il8W5Ab1UGzLS6f3_VoQ322rEmDBrKruykvzQj_GlGIH0ozXc2JDZpLRvnzwNaYDGgqA3ro4AYXBfYS-4n4X0RDdqiX1Ug'
request = requests.get(link.format(39783), headers={'Authorization': f'Bearer {token}'})
respond = request.json()
print(respond.keys())
print(json.dumps(respond, indent=True))

# anime_id = 39783
# data = {
#     "status": watching,
#     "score": 10,
#     "num_watched_episodes": 12
# }
# response = requests.put(UPDATE_ALIST.format(anime_id), data=data,
#                         headers={'Authentication': f'Bearer {token}'})
# response.raise_for_status()
# print(response.json())
#YA EBAL V ROT ETI PV. 2.5k strok ebanutiy chel