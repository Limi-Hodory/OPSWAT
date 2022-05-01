from sys import argv
import sys
import AnalyzeFile
import argparse
import time



def parse_arguments():
    parser = argparse.ArgumentParser()

    # Required Arguments
    parser.add_argument("-host", "--host", dest="host",  required=True, 
                        help="Specify the host")
    parser.add_argument("-k", "--key", dest="apikey", required=True,
                        help="Unique API key to give rights to use endpoint")
    parser.add_argument("-f", "--file", dest="file", required=True,
                        help="Specify a file location that should be scanned")

    # Non required Arguments
    parser.add_argument("-n", "--name", dest="name", required=False, default=None,
                        help="flag to preserve file name in scan")
    #archivepwd
    parser.add_argument("-p", "--password", dest="pwd", required=False, default=None,
                        help="password if submitted file is password protected (archive pwd)-not required ")

    #active workflows (mcl-metadefender-rest-sanitize-disabled-unarchive)
    parser.add_argument("-w", "--workflow", dest="workflow", default="File process",
                        help="active workflows, allowed values: File process-mcl-metadefender-Kiosk-Meta-Defender Vault-disabled-unarchive")

    args = parser.parse_args()
    validate(args)
    return args


def validate(args):
    '''
    validate given args based on arg criteria
    input:
        args: inputted arguments
    '''

    workflow_values = ['File process','mcl', 'metadefender', 'Kiosk', 'MetaDefender Vault', 'disabled', 'unarchive']
    if args.workflow and args.workflow not in workflow_values:
        print("Invalid workflow variable given, allowed values: File process-mcl-metadefender-Kiosk-Meta-Defender Vault-disabled-unarchive")
        sys.exit(0)


if __name__ == '__main__':
    args = parse_arguments()

    host=args.host
    apikey= args.apikey 
    try:
        f= open(args.file , "rb")#read binary
        file= f.read()
    except IOError:
            print("File not accessible, check the file path")
    file_name= args.name
    workflow= args.workflow
    archive_pwd= args.pwd

    # Extract data id of the file to scan
    data_id= AnalyzeFile.scan_file_asyn(host,apikey, file, file_name,workflow,archive_pwd)
    scan_result= AnalyzeFile.get_file_info(host,data_id,apikey)
    print("\nScaning in Progress")
    while scan_result["scan_results"]["current_av_result_a"] == "In Progress":
        scan_result = AnalyzeFile.get_file_info(host,data_id,apikey)
    print("\nScaning in Progress\n")
    scan_result= AnalyzeFile.get_file_info(host,data_id,apikey)
    time.sleep(2)
    print(AnalyzeFile.display_results(scan_result))
    

