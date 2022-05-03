#Delete hashes from 'skip by hash' list
import requests
import pandas as pd


def delete_from_blocklist(hashes_file_path, apikey, host):
    try:
        df = pd.read_csv(hashes_file_path)
    except Exception:
        print("\nIncorrect file path/file does not exist")
        return
    for i in range(len(df)) : #Foreach row in the hashes file- send the row to blocklist
        hash=df.loc[i, "hash"]  
        apicall(hash,apikey,host)


def apicall(hash,apikey,host):
    url = f"http://{host}:8008/admin/config/skip"
    headers = {
     "Content-Type": "application/json",
     "apikey": apikey
    }
    payload =  payload = f"[\"{hash}\"]"
    response = requests.request("DELETE", url, headers=headers, data=payload)
    if response.status_code !=200: #Check if the request was successful
        raise Exception(f"\nrequest filed with status code: {response.status_code}")
    print("Deletion completed")
    return(response.text)

