import requests
client_key="REDACTED"

class zc_account:
    def __init__(self, zc, items):

        if zc is None:
            self.zc = 0
        else:
            self.zc = zc

        if not items:
            self.items = None
        else:
            self.items = items

    def __str__(self):
        return f"{self.zc}ZC with items: {self.items}"

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NoAccountException(Error):
    def __init__(self, _id, response):
        self.id = _id
        self.response = response

class ServerResponseException(Error):
    def __init__(self, code, response):
        self.status_code = code
        self.response = response


def lookup(_id):
    URL = f"https://www.zolts.ga/api/check/get_user?client_key={client_key}&id={_id}"

    r = requests.get(URL)
    if (r.headers['Content-Type'] != "application/json") or (r.status_code != 200):
        raise ServerResponseException(requests.status_codes._codes[r.status_code][0], r.text)

    j = r.json()
    if "ERROR" in j.keys():
        err = j["ERROR"]
        if err == "invalid_id":
            raise NoAccountException(id, err)
        else:
            raise ServerResponseException(requests.status_codes._codes[r.status_code][0], err)

    finance = j["zolts_account"]["finance"]
    return zc_account(finance["zc"], finance["items"])
