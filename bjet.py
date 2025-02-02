# post example bsky

import sys
import os

import bjet_config as config

script_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f'{script_path}/{config.APP_NAME}')

import client
import post
import menu
import bjetlog



def write_post():
    conn, user = client.setup()
    menu.splash()

    print('type \'cancel\' to cancel your post\n')
    text_color = menu.color('yellow')
    post_text = input(f'What\'s up ?\n\n{text_color}')
    print(menu.color('end'))

    if post_text == 'cancel':
        main_menu()

    post.send_post(
        conn,
        user.username,
        post_text
    )
    main_menu()


def edit_login():
    menu.user_info()
    client.setup(override_userdata=True)
    main_menu()

def logout():
    exit()


def main_menu():
    menu.splash()
    menu.user_info()
    options = menu.build_options()

    user_input = ''
    try:
        while user_input not in options.keys():
            user_input = input('Enter Option: ')
            print(user_input)
            if user_input == '1':
                write_post()
            elif user_input == '2':
                edit_login()
            elif user_input == '3':
                logout()
            else:
                print('INCORRECT INPUT !\n\n')

        input('wait')
    except Exception as e:
        print(e)


def main():
    menu.initial_loadup()

    # check login information and that client can be connected
    _, user = client.setup()
    menu.username = user.username

    main_menu()



if __name__ == '__main__':
    main()
