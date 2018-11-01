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
