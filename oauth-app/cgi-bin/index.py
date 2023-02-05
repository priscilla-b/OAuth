#!/usr/bin/env python
# shebang line here not needed on a windows os
import os
import json
import requests
import secrets
import urllib.parse
import webbrowser

from dotenv import load_dotenv



load_dotenv()

def api_request(url, post=False, headers={}):
    default_headers = {
        'Accept': 'application/vnd.github.v3+json, application/json',
        'User-Agent': 'http://localhost:8000/'
    }

    if 'access_token' in headers:
        default_headers['Authorization'] = 'Bearer ' + headers['access_token']
    headers = default_headers

    if post:
        response = requests.post(url, headers=headers, data=json.dumps(post))
    else:
        response = requests.get(url, headers=headers)

    return response.json()

# url = "http://localhost:5000/"

github_client_id = os.environ.get('GITHUB_CLIENT_ID')
github_client_secret = os.environ.get('GITHUB_CLIENT_SECRET')

#  url to get a user's authorization
authorize_url = 'https://github.com/login/oauth/authorize'

# endpoint to request an access token
token_url = 'https://github.com/login/oauth/access_token'

# github base url for api requests
api_url_base = 'https://api.github.com/'

# url for this script, used as the redirect url
base_url = 'http://' + os.environ.get('HOST_NAME', 'localhost') + '/'

# start a session so we have a place to store things between redirects
session = requests.Session()


access_token = os.environ.get('ACCESS_TOKEN')

print("Content-type:text/html\r\n\r\n")
# necessary to set the content type of the response to "text/html"
# the "\r\n\r\n" is used to indicate the end of the HTTP headers 
# and the start of the content body.

if 'action' not in os.environ:
    # the action environment variable is used as a query parameter is the given url
    # to determine the desired action of the user. e.g. login,repos, logout
    # here action, is used to determine is user is logged in or not.
    # if action is not present, code checks if user is already logged 
    # in by checking the access token
    if access_token:
        print('Logged In')
        print('<p><a href="?action=repos">View Repos</a></p>')
        print('<p><a href="?action=logout">Log Out</a></p>')
    else:
        print('Not logged in')
        print('<p><a href="?action=login">Log In</a></p>')
    exit()


# Start the login process by sending the user
# to GitHub's authorization page
if 'action' in os.environ and os.environ['action'] == 'login':
    os.environ['ACCESS_TOKEN'] = ''

    # Generate a random hash and store in the environment
    state = secrets.token_hex(16)
    os.environ['STATE'] = state
    
    # parameters to send to the GitHub authorization page
    params = {
        'response_type': 'code',
        'client_id': github_client_id,
        'redirect_uri': base_url,
        'scope': 'user public_repo',
        'state': state
    }

    # Redirect the user to GitHub's authorization page
    authorize_url = f"{authorize_url}?{urllib.parse.urlencode(params)}"
    # urllib.parse.urlencode encodes the params as a query string

    webbrowser.open(authorize_url)
    exit()
