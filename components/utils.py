import json
import os


def get_config():
    if not os.path.exists(os.getcwd() + "\config.json"):
        return {}
    else:
        with open("config.json", "r") as f:
            data = json.loads(f.read())
            return data





SAVED_CONFIG = get_config()
