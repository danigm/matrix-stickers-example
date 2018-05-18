import requests
from urllib.parse import urlencode

URL = "https://matrix.org/_matrix/client/r0/"
VURL = "https://scalar.vector.im/api/"

def mx(path="", method="GET", data={}):
    token = open("token").read().strip()

    url = "{}{}?access_token={}".format(URL, path, token)
    if method == "GET":
        if data:
            url += "&" + urlencode(data)
        resp = requests.get(url, headers={"Content-Type": "application/json"})
    else:
        q = getattr(requests, method.lower())
        resp = q(url, json=data)

    return resp.json()


def vx(path="", method="GET", data={}):
    token = open("scalar_token").read().strip()

    url = "{}{}?scalar_token={}".format(VURL, path, token)
    if method == "GET":
        if data:
            url += "&" + urlencode(data)
        resp = requests.get(url, headers={"Content-Type": "application/json"})
    else:
        q = getattr(requests, method.lower())
        resp = q(url, json=data)

    return resp.json()
