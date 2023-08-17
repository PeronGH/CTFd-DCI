import os
import requests

BASE_URL = os.environ.get("BASE_URL", "http://spawn:8000")


def list_instances():
    r = requests.get(f"{BASE_URL}/instances")
    return r.json()
