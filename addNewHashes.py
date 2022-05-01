from ast import Add
import json
import pandas as pd
import requests
import time

# Input - list (block/alllow) and hash to put on the list
# Output - a list of all skip/white/black-listed hashes.
def api_call(list,hash, comment, apikey, host):
    url = f"http://{host}:8008/admin/config/skip"
    payload = "{\""+list+"\": {\""+hash+"\": {\"comment\": \"" +comment+"\"}}}"
    headers = {
         "Content-Type": "application/json",
         "apikey": apikey
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code !=200: #Check if the request was successful
        raise Exception(f"\nrequest filed with status code: {response.status_code}")
    return response.text

# Add hashes file to block list
def add_to_blocklist(hashes_file_path,apikey,host):
    result=""
    try:
        df = pd.read_csv(hashes_file_path)
    except Exception:
        print("\nIncorrect file path/file does not exist\n")
        return
    for i in range(len(df)) : #Foreach row in the hashes file- send the row to blocklist
        hash=df.loc[i, "hash"] 
        comment=df.loc[i, "comment"] 
        try:
            api_call("blacklist",hash,comment,apikey,host)
            time.sleep(2)
            result+= f"Hash: {hash}, comment: {comment}\n was successfully added to the blocklist\n\n "
        except Exception as e:
            print(e)
            print(f"failed to add hash: {hash}\n")
    return result 

# Add hashes file to allow list
def add_to_whitelist(hashes_file_path,apikey,host):
    result=""
    try:
        df = pd.read_csv(hashes_file_path)
    except Exception:
        print("\nIncorrect file path/file does not exist\n")
        return
    for i in range(len(df)) : #Foreach row in the hashes file
        hash=df.loc[i, "hash"] 
        comment=df.loc[i, "comment"] 
        try:
            api_call("whitelist",hash,comment,apikey,host)
            time.sleep(2)
            result+= f"Hash: {hash}, comment: {comment}\n was successfully added to the allow list\n\n "
        except Exception as e:
            print(e)
            print(f"failed to add hash: {hash}\n")
    return result 



