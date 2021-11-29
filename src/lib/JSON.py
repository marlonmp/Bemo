import json
import os

def parse_file(path: str, default_content: str='{}') -> dict:

    if not os.path.exists(path):
        with open(path, 'w+') as file:
            file.write(default_content)
    
    with open(path, 'r') as file:

        dict = json.loads(file.read())

        return dict

def stringify_file(path: str, dict: dict):
    
    jsonStr = json.dumps(dict)

    with open(path, 'w+') as file:
        file.write(jsonStr)