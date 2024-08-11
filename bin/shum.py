
import os
import sys
import json
import shutil
import tempfile
from pathlib import Path

HOME = os.path.expanduser('~')
DATABASE = Path(f'{HOME}/.local/share/sharkumbrella/data.json')
DATABASE.parent.mkdir(parents=True, exist_ok=True)

try:
    COLLECTION = Path(os.environ['COLLECTION'])
except KeyError:
    print('please set the COLLECTION variable in your environment', file=sys.stderr)
    sys.exit(1)

# constants
A_FACTOR = 2.5

def parse_stdin():
    return [i.strip() for i in sys.stdin.readlines()] if not sys.stdin.isatty() else None

def recursive_scandir(directory):
    for entry in os.scandir(directory):
        if entry.is_dir(follow_symlinks=False):
            yield from recursive_scandir(entry.path)
            continue 

        yield entry 

def safe_write(data, path):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = Path(temp_dir) / path.name
        
        with temp_file.open('w', encoding='utf-8') as f:
            json.dump(data, f)
        
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(temp_file), str(path))

        return path

def load_data():
    try:
        with open(DATABASE, 'r') as f:
            return json.load(f) 
    except FileNotFoundError:
        return {}

def relative_path(path):
    try:
        return str(path.relative_to(COLLECTION))
    except ValueError:
        return None 

def is_in_coll(path):
    try:
        relative_path = path.relative_to(COLLECTION)
        return True
    except ValueError:
        return False
