import requests
from getpass import getpass


# Login- return sid as a string
def login(host):
    user=input("Please enter username: ")
    password = getpass()
    url = f"http://{host}:8008/login"
    headers = {
    "Content-Type": "application/json"
    }
    payload = "{\"user\":\""+user+"\",\"password\":\""+password+"\"}"
    # If username/pass incorrect
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        session_id= response.json()
        return session_id["session_id"]
    except Exception:
        print("Incorrect username or password")
    

