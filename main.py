import requests
import sys

def loop():
    for word in sys.stdin:
        res = requests.get(url=f"http://10.10.11.161/{word}")
        if res.status_code == 404:
            loop()
        else:
            data = res.json()
            print(data)
            print(res.status_code)

loop()
#cat common.txt| python fuzz.py
