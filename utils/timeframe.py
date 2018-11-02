import re
import calendar
import time
translations = {("s","sec","secs","second","seconds"):1,
                ("m","min","mins","minute","minutes"):60,
                ("h","hour","hours"):3600,
                ("d","day","days"):86400,
                ("w","week","weeks"):604800,
                ("m","month","months"):2592000,
                ("y","yrs","year","years"):31622400}

def convert(raw):
    duration, timeframe = list(filter(None, re.split('(\d+)',raw)))

    for keys, _ in translations.items():
        if timeframe in keys:
            return (calendar.timegm(time.gmtime())) + (int(duration)*translations[keys])
    raise KeyError(f"Timeframe '{timeframe}' not found. Type !help timeframes for a list.")

def seconds(s):
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    if all(i == 0 for i in [m,h,d]):
        return f"{s} second{'s' if s != 1 else ''}"
    elif all(i == 0 for i in [h,d]):
        return f"{m} minute{'s' if m != 1 else ''} and {s} second{'s' if s != 1 else ''}"
    elif d == 0:
        return f"{h} hour{'s' if h != 1 else ''}, {m} minute{'s' if m != 1 else ''} and {s} second{'s' if s != 1 else ''}"
    else:
        return f"{d} day{'s' if d != 1 else ''}, {h} hour{'s' if h != 1 else ''}, {m} minute{'s' if m != 1 else ''} and {s} second{'s' if s != 1 else ''}"
