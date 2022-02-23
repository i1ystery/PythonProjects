from datetime import datetime

import requests

from ChallengeCodeGenerator import *


APP_CLIENT_ID = '94b8cda0926111099fd079126ee497e7'
APP_CLIENT_SECRET = '8ada8a9ff8547c2cb156a790af7741b93f074c8c6beaef5364047dbd3d82f5d5'
CHALLENGE_CODE = CODE_VERIFIER = None


def generate_authorization_link():
    global CHALLENGE_CODE, CODE_VERIFIER
    CHALLENGE_CODE = CODE_VERIFIER = get_new_code_verifier()
    return f'https://https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={APP_CLIENT_ID}&code_challenge={CHALLENGE_CODE}'


def generate_new_user_token(auth_code: str, code_verifier: str) -> dict:
    url = 'https://myanimelist.net/v1/oauth2/token'
    data = {
        'app_client_id': APP_CLIENT_ID,
        'app_client_secret': APP_CLIENT_SECRET,
        'auth_code': auth_code,
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
        'app_client_id': APP_CLIENT_ID,
        'app_client_secret': APP_CLIENT_SECRET,
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
