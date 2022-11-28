from flask import Flask, redirect, request, session
from dotenv import load_dotenv
import requests
import json
import os
import sys

load_dotenv()
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

app = Flask(__name__)


@app.route('/')
def request_auth():  # put application's code here
    scope = 'user-top-read playlist-modify-public playlist-modify-private user-follow-read'
    return redirect(f'https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={scope}')


@app.route('/callback')
def request_tokens():
    code = request.args.get('code')

    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    r = requests.post(SPOTIFY_TOKEN_URL, data=payload)
    response = r.json()

    tokens = {
        'access_token': response['access_token'],
        'refresh_token': response['refresh_token'],
        'expires_in': response['expires_in']
    }

    with open('tokens.json', 'w') as outfile:
        json.dump(tokens, outfile)

    return 'Authorization flow complete'


@app.route('/get_artists')
def get_artists():
    pass


@app.route('/get_albums')
def get_albums():
    pass


@app.route('/get_tracks')
def get_tracks():
    pass


@app.route('/create_playlist')
def create_playlist():
    pass


@app.route('/add_to_playlist')
def add_to_playlist():
    pass


if __name__ == '__main__':
    app.run()
