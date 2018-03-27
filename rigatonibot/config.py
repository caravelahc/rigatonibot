import json

from os import environ
from pathlib import Path

try:
    CONFIG_DIR = Path(environ['XDG_CONFIG_HOME'], 'rigatonibot')
except KeyError:
    CONFIG_DIR = Path.home() / '.config' / 'rigatonibot'

try:
    with open(CONFIG_DIR / 'config.json') as f:
        config = json.load(f)
except FileNotFoundError:
    config = {}

TOKEN = config['token']
