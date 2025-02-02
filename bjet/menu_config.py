# menu config

import os

script_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(script_path)

# color list
COLOR_LIST = {
    'red': '\33[91m',
    'blue': '\33[94m',
    'green': '\033[32m',
    'yellow': '\033[93m',
    'purple': '\033[0;35m',
    'cyan': '\033[36m',
    'end': '\033[0m'
}

# splash banner
BANNER = f'''{COLOR_LIST["blue"]}

██████╗      ██╗███████╗████████╗
██╔══██╗     ██║██╔════╝╚══██╔══╝
██████╔╝     ██║█████╗     ██║
██╔══██╗██   ██║██╔══╝     ██║
██████╔╝╚█████╔╝███████╗   ██║
╚═════╝  ╚════╝ ╚══════╝   ╚═╝
{COLOR_LIST["end"]}
'''

MENU_OPTIONS = {
    '1': 'write_post',
    '2': 'edit_login',
    '3': 'logout',
}

MOTD_LIST = [
    'warning: may contain nuts',
    'sexy',
    'made in the basement',
    'where the skies are blue',
    'the everything app',
    'i heard a qt made this'
]

WPM = 80

BOOT_SOUND = f'{parent_path}/media/sound1.mp3'
