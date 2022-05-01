# Get 'skip by hash' list
from tkinter import Frame
import requests
import pandas as pd
import json

# Returns data Frame
def get_hashes_list(host,apikey):
    url =f"http://{host}:8008/admin/config/skip"
    headers = {
     "apikey": apikey
    }
    response = requests.request("GET", url, headers=headers)
    convertedDict = json.loads(response.text)
    df=pd.DataFrame.from_dict(convertedDict)
    return df

