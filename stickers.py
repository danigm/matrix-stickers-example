#!/usr/bin/env python3

from mx import mx
from mx import vx

USER = "USERID"
USERID = "@USERID:matrix.org"
PASSWORD = "******"

def stickerlist():
    # list all stickers
    resp = vx("widgets/assets", data={"widget_type": "m.stickerpicker", "widget_id": WIDGET_ID, "filter_unpurchased": True})
    print("STICKER LIST:")
    for s in resp["assets"]:
        print(" * {name}, {purchased}".format(**s))
        if s["purchased"]:
            print("    IMAGES:")
            for img in s["data"]["images"]:
                print("    * {name}".format(**img))


data={
  "initial_device_display_name": "dirty script",
  "type": "m.login.password",
  "user": USER,
  "password": PASSWORD,
}
# login
resp = mx("login", method="POST", data=data)
with open('token', 'w') as f:
    f.write(resp["access_token"])

# registering in the scalar.vector.im
resp = mx("user/{}/openid/request_token".format(USERID), method="POST")
resp = vx("register", method="POST", data=resp)
with open('scalar_token', 'w') as f:
    f.write(resp["scalar_token"])

# GET widget id
data = { "data": {}, "type": "m.stickerpicker", }
resp = vx("widgets/request", method="POST", data=data)
WIDGET_ID = resp.get("id") or resp["data"]["id"]

# list all stickers
stickerlist()

# purchase one
resp = vx("widgets/added", method="POST", data={"type": "m.stickerpicker"})
data = {
    "asset_type": "stickman",
    "widget_type": "m.stickerpicker",
    "widget_id": WIDGET_ID,
}
resp = vx("widgets/purchase_asset", data=data)

stickerlist()

## remove one
data = {
    "asset_type": "stickman",
    "state": "disable",
    "widget_id": WIDGET_ID,
    "widget_type": "m.stickerpicker",
}
resp = vx("widgets/set_asset_state", data=data)

stickerlist()
