import requests, json
import sys
from sys import argv


def scan_file_asyn(host,apikey, file, filename ,workflow="File process", archive_pwd=None):
    url = f"http://{host}:8008/file"
    headers = {
     "Content-Type": "application/octet-stream",
     "apikey": apikey,
     "filename": filename,
     "workflow": workflow,
     "archivepwd": archive_pwd
    }
    payload = file
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code !=200: #Check if the request was successful
        raise Exception(f"\nrequest filed with status code: {response.status_code}")
    return response.json()["data_id"]


def scan_file_syn(host,apikey, file, filename ,workflow="File process", archive_pwd=None):
        url = f"http://{host}:8008/file/sync"
        headers = {
         "Content-Type": "application/octet-stream",
         "apikey": apikey,
         "filename": filename,
         "workflow": workflow,
         "archivepwd": archive_pwd
        }
        payload = file
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()["data_id"]

# Return all the info about the file
def get_file_info(host, data_id, apikey):
    url = f"http://{host}:8008/file/{data_id}"
    payload={}
    headers = {
      'apikey': apikey
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code !=200: 
        raise Exception(f"\nrequest filed with status code: {response.status_code}")
    return response.json()


# Get scan results from get file info
def display_results(result):
    scan_result=result["scan_results"]["current_av_result_a"]
    data_id= result["data_id"]
    file_name= result["file_info"]["display_name"] #check if there is a name
    file_type= result["file_info"]["file_type"]
    md5= result["file_info"]["md5"]
    sha1=result["file_info"]["sha1"]
    sha256= result["file_info"]["sha256"]
    is_blocked= result["process_info"]["result"]
    blocked_reasons=result["process_info"]["blocked_reasons"] #if null (" ") not blocked
    string=""
    string+= f"Scan resulte: {scan_result}\n"
    if file_name!="":
        string+= f"File name: {file_name} \n"
    string+=f"Data id: {data_id}\n"
    string+=f"File type: {file_type}\n"
    string+=f"File hash info: \nmd5:{md5} \nsha1: {sha1} \nsha256:{sha256}\n"
    if is_blocked== "Blocked":
        string+= f"The file was blocked, blocked reasons: {blocked_reasons}\n"
    return string


# result= get_file_info(host,"6adef5f24f6e4085bf81ac06778e9ecc",apikey)
# print(display_results(result))
