import requests

API_KEY = "YOUR API KEY GOES HERE"

def headers():
    headers = {
        "accept": "application/json",
        "x-api-key": API_KEY,
        "Content-Type": "application/json",
    }

    return headers

def json_data(twitter_handle):
    json_data = {
        "name": twitter_handle,
        "how": "username",
        "page": 1,
    }

    return json_data

def get_follower_count(twitter_handle):

    response = requests.post('https://toto.oz.xyz/api/metadata/get_follower_count', headers=headers(), json=json_data(twitter_handle)).json()
    return response

def get_metadata_history(twitter_handle):

    response = requests.post('https://toto.oz.xyz/api/metadata/get_metadata_history', headers=headers(), json=json_data(twitter_handle)).json()
    return response

def get_userid(twitter_handle):

    response = requests.post('https://toto.oz.xyz/api/metadata/get_userid', headers=headers(), json=json_data(twitter_handle)).json()
    return response

def get_followers(twitter_handle):

    response = requests.post('https://toto.oz.xyz/api/graph/get_followers', headers=headers(), json=json_data(twitter_handle)).json()
    return response

def get_following(twitter_handle):

    response = requests.post('https://toto.oz.xyz/api/graph/get_following', headers=headers(), json=json_data(twitter_handle)).json()
    return response

def get_score_history(twitter_handle):

    response = requests.post('https://toto.oz.xyz/api/models/get_score_history', headers=headers(), json=json_data(twitter_handle)).json()
    return response

