import requests
from getpass import getpass

def change_pass(host, apikey):
    old_pass=input("Please enter current passord: ")
    new_pass= getpass("Please enter new passord: ")
    url = f"http://{host}:8008/user/changepassword"
    headers = {
     "Content-Type": "application/json",
     "apikey": apikey
     }
    payload = "{\"old_password\":\""+old_pass+"\",\"new_password\":\""+new_pass+"\"}"
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

