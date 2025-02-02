import os
import logging

script_path = os.path.dirname(os.path.abspath(__file__))

log = logging.getLogger(__name__)
logging.basicConfig(
    filename=f'{script_path}/logs/bjet.log',
    level=logging.INFO
)
