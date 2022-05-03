from unittest import result
import loginOpswat
import changePassword
import getList
import addNewHashes
import deleteHashes
import AnalyzeFile
import logout
import time
from getpass import getpass
import os


host=input("Enter the host: ")
apikey= getpass("Enter your apikey (if you don't have an apikey enter \"log\"): ") #secret string
if apikey=="log":
    apikey=loginOpswat.login(host)
    print("Login successfully")
def menu():
    print("\n[1] Login")
    print("[2] Logout")
    print("[3] Change Password")
    print("[4] Get 'skip by hash' list")
    print("[5] Add new hashes to Blocklist")
    print("[6] Add new hashes to Allowlist ")
    print("[7] Delete hashes from 'skip by hash' list")
    print("[8] Scan file asyn")
    print("[9] Scan file syn")
    print("[0] Exit\n")

menu()
option=int(input("Enter your choice: "))

while option!=0:
    if option==1:
        apikey=loginOpswat.login(host)
        print("Login successfully")
    elif option==2:
        logout.Logout(host, apikey)
    elif option==3:
        changePassword.change_pass(host, apikey)
        print("changed successfully")
    elif option==4:
        print(getList.get_hashes_list(host, apikey))
    elif option==5:
        hashes_file_path= input("Enter hashes file location: ")
        stripped_string = hashes_file_path.strip('"') #remove quotes
        print(addNewHashes.add_to_blocklist(stripped_string,apikey,host))
    elif option==6:
        hashes_file_path= input("Enter hashes file location: ")
        stripped_string = hashes_file_path.strip('"') #remove quotes
        print(addNewHashes.add_to_whitelist(stripped_string,apikey,host))
    elif option==7:
        hashes_file_path= input("Enter hashes file location: ")
        stripped_string = hashes_file_path.strip('"')
        deleteHashes.delete_from_blocklist(stripped_string, apikey, host)
    elif option==8:
        file_path= input("Enter file location: ")
        stripped_string = file_path.strip('"') #remove quotes
        try:
            f= open(stripped_string, "rb")#read binary
            file= f.read()
            file_name=os.path.basename(stripped_string) #extract file name
            data_id=AnalyzeFile.scan_file_asyn(host,apikey, file, file_name)
            print("\nScaning in Progress")
            scan_result= AnalyzeFile.get_file_info(host,data_id,apikey)
            while scan_result["scan_results"]["current_av_result_a"] == "In Progress":
                scan_result = AnalyzeFile.get_file_info(host,data_id,apikey)
            scan_result= AnalyzeFile.get_file_info(host,data_id,apikey)
            print("\nScaning in Progress\n")
            time.sleep(2)
            print(AnalyzeFile.display_results(scan_result))
        except IOError:
            print("\nFile not accessible, check the file path\n")        
    elif option==9:
        file_path= input("Enter file location: ")
        stripped_string = file_path.strip('"') #remove quotes
        try:
            f= open(stripped_string, "rb")#read binary
            file= f.read()
            file_name=os.path.basename(stripped_string)
            data_id=AnalyzeFile.scan_file_syn(host,apikey, file, file_name)
            print("\nScaning in Progress")
            scan_result= AnalyzeFile.get_file_info(host,data_id,apikey)
            while scan_result["scan_results"]["current_av_result_a"] == "In Progress":
                scan_result = AnalyzeFile.get_file_info(host,data_id,apikey)
            scan_result= AnalyzeFile.get_file_info(host,data_id,apikey)
            print("\nScaning in Progress\n")
            time.sleep(2)
            print(AnalyzeFile.display_results(scan_result))
        except IOError:
            print("\nFile not accessible, check the file path\n")  
    else:
        print("\nInvalid option")

    print()        
    menu()
    option=int(input("\nEnter your choice: "))

print("GOODBYE")
