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


host=input("Enter the host: ")
apikey= getpass("Enter your apikey (if you don't have an apikey enter \"log\"): ") #secret string
if apikey=="log":
    apikey=loginOpswat.login(host)
    print("Login successfully")
def menu():
    print("\n[0] Exit")
    print("[1] Login")
    print("[2] Change password")
    print("[3] Get 'skip by hash' list")
    print("[4] Add new hashes to blocklist")
    print("[5] Add new hashes to allowlist ")
    print("[6] Delete hashes from 'skip by hash' list")
    print("[7] Scan file asyn")
    print("[8] Scan file syn")
    print("[9] Logout\n")

menu()
option=int(input("Enter your choice: "))

while option!=0:
    if option==1:
        apikey=loginOpswat.login(host)
        print("Login successfully")
    elif option==2:
        changePassword.change_pass(host, apikey)
        print("changed successfully")
    elif option==3:
        print(getList.get_hashes_list(host, apikey))
    elif option==4:
        hashes_file_path= input("Enter hashes file location: ")
        stripped_string = hashes_file_path.strip('"') #remove quotes
        print(addNewHashes.add_to_blocklist(stripped_string,apikey,host))
    elif option==5:
        hashes_file_path= input("Enter hashes file location: ")
        stripped_string = hashes_file_path.strip('"') #remove quotes
        print(addNewHashes.add_to_whitelist(stripped_string,apikey,host))
    elif option==6:
        hashes_file_path= input("Enter hashes file location: ")
        deleteHashes.delete_from_blocklist(hashes_file_path, apikey, host)
    elif option==7:
        file_path= input("Enter file location: ")
        stripped_string = file_path.strip('"') #remove quotes
        try:
            f= open(stripped_string, "rb")#read binary
            file= f.read()
        except IOError:
            print("File not accessible, check the file path")
        file_name=input("Enter file name: ")
        print("\nScaning in Progress")
        data_id=AnalyzeFile.scan_file_asyn(host,apikey, file, file_name)
        scan_result= AnalyzeFile.get_file_info(host,data_id,apikey)
        while scan_result["scan_results"]["current_av_result_a"] == "In Progress":
            scan_result = AnalyzeFile.get_file_info(host,data_id,apikey)
        scan_result= AnalyzeFile.get_file_info(host,data_id,apikey)
        print("\nScaning in Progress\n")
        time.sleep(2)
        print(AnalyzeFile.display_results(scan_result))
        # print(AnalyzeFile.display_results(host, data_id ,apikey))
    elif option==8:
        file_path= input("Enter file location: ")
        stripped_string = file_path.strip('"') #remove quotes
        try:
            f= open(stripped_string, "rb")#read binary
            file= f.read()
        except IOError:
            print("File not accessible, check the file path")
        file_name=input("Enter file name: ")
        print("\nScaning in Progress")
        data_id=AnalyzeFile.scan_file_syn(host,apikey, file, file_name)
        scan_result= AnalyzeFile.get_file_info(host,data_id,apikey)
        while scan_result["scan_results"]["current_av_result_a"] == "In Progress":
            scan_result = AnalyzeFile.get_file_info(host,data_id,apikey)
        scan_result= AnalyzeFile.get_file_info(host,data_id,apikey)
        print("\nScaning in Progress\n")
        time.sleep(2)
        print(AnalyzeFile.display_results(scan_result))
    elif option==9:
        logout.Logout(host, apikey)    
    else:
        print("\nInvalid option")

    print()        
    menu()
    option=int(input("\nEnter your choice: "))

print("GOODBYE")









