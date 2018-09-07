import requests
client_key="REDACTED"

class account:
    def __init__(self, zc, items):

        if zc == None:
            self.zc = 0
        else:
            self.zc = zc

        if len(items) == 0:
            self.items = None
        else:
            self.items = items

    def __str__(self):
        return f"{self.zc}ZC with items: {self.items}"

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NoAccountException(Error):
    def __init__(self, id, response):
        self.id = id
        self.response = response

class ServerResponseException(Error):
    def __init__(self, response):
        self.response = response


def lookup(id):
    URL = f"https://www.zolts.ga/api/check/get_user?client_key={client_key}&id={id}"

    r = requests.get(URL)
    if (r.headers['Content-Type'] != "application/json") or (r.status_code != 200):
        if r.status_code != 200:
            raise ServerResponseException(requests.status_codes._codes[r.status_code][0])
        else:
            raise ServerResponseException(r.text)

    j = r.json()
    if "ERROR" in j.keys():
        err = j["ERROR"]
        if err == "invalid_id":
            raise NoAccountException(id, err)

    finance = j["zolts_account"]["finance"]
    return account(finance["zc"], finance["items"])
