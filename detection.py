import time
import requests

while True:
    requests.get("http://127.0.0.1:5000/update/1")
    print("Animal detectado")
    time.sleep(5)

    requests.get("http://127.0.0.1:5000/update/0")
    print("Animal ausente")
    time.sleep(5)