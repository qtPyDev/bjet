# setup client for bsky

import os
import json
import bjet_config as config

from bjetlog import log

from getpass import getpass
from atproto import Client



class User:
    def __init__(self):
        self.username = ''
        self.password = ''


def login():
    user = User()
    user.username = input('Username: ')
    user.password = getpass('Password: ')
    return user


def establish_session(user):
    client = None
    try:
        client = Client()
        client.login(user.username, user.password)
    except Exception as e:
        log.info(e)
        print('username or password was incorrect')
        print('please try again')
        print('\n')
        setup(override_userdata=True)

    return client


def get_user():
    if not os.path.exists(config.DATA_PATH):
        return

    user = User()
    with open(config.DATA_PATH, 'r') as file:
        userdata = json.load(file)
        user.username = userdata['username']
        user.password = userdata['password']

    return user


def write_userdata(user):
    user_data = {
        'app': config.APP_NAME,
        'username': user.username,
        'password': user.password
    }

    data_path_dir = os.path.dirname(config.DATA_PATH)
    if not os.path.exists(data_path_dir):
        os.makedirs(data_path_dir)

    # allow for overwritting
    open_type = 'w'
    # if os.path.exists(config.DATA_PATH):
    #     open_type = 'a'

    with open(config.DATA_PATH, open_type) as file:
        json.dump(user_data, file, indent=4)


def setup(override_userdata=False):
    user = None
    if override_userdata == False:
        user = get_user()

    if not user:
        user = login()
        write_userdata(user)

    client = establish_session(user)
    return client, user
