import requests

def Logout(host, apikey):
    url = f"http://{host}:8008/logout"
    headers = {
    "apikey": apikey
    }
    response = requests.request("POST", url, headers=headers)
    return response.text
