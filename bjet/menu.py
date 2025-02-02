import os
import sys
import random
from pygame import mixer
from time import gmtime, strftime, sleep

import menu_config as config


current_user = ''


def splash():
    motd = random.choice(config.MOTD_LIST)

    os.system('cls' if os.name=='nt' else 'clear')
    print(config.BANNER)
    print(color('yellow'))
    slow_type(f'{motd} !')
    print(color('end'))


def initial_loadup():
    os.system('cls' if os.name=='nt' else 'clear')

    mixer.init()
    mixer.music.load(config.BOOT_SOUND)
    mixer.music.play()

    slow_type(
        text=config.BANNER,
        speed=250
    )


def build_options():
    options = config.MENU_OPTIONS
    for key, option in options.items():
        option_text = option.replace('_', ' ').title()
        print(f'{key}). {option_text}')

    print('\n')

    return options


def user_info():
    current_time = strftime('%H:%M', gmtime())
    current_date = strftime('%d-%m-%Y', gmtime())

    print(color('yellow'))
    print(f'Welcome to Bluesky {current_user}')
    print(f'Time: {current_time}')
    print(f'Date: {current_date}')
    print(color('end'))


def color(color_text):
    colors = config.COLOR_LIST
    for color, code in colors.items():
        if color == color_text:
            return code

    return ''


def slow_type(text, speed=config.WPM):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(random.random()*10.0/speed)
    print('')
