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
    if response.status_code !=200: #Check if the request was successful
        raise Exception(f"\nrequest filed with status code: {response.status_code}")
    my_dict= response.json()
    print("\nblacklist:\n")
    print(pd.DataFrame.from_dict(my_dict)['blacklist'])
    print("\nwhitelist:\n")
    print(pd.DataFrame.from_dict(my_dict)['whitelist'])
    return

