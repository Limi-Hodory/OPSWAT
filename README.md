# OPSWAT
Easy-to-use interface in OPSWAT that includes adding hashes to block\allow list, scanning files and more...

### Requirements:

Python 3.10

## Installation

```
pip install -r requirements.txt
```
## Example 1 (recommended)
```
python main.py
```
<img width="356" alt="image" src="https://user-images.githubusercontent.com/83369474/166484243-5ca73901-d57e-42eb-8cd6-d0ff08868514.png">

## Example 2
```
python scanFile.py -h 10.0.0.168 -k apikey -f "C:\Users\file.txt" 
```
## Example 3
```
python scanFile.py -h 10.0.0.168 -k apikey -f "C:\Users\file.txt" -w workflow -p archive pwd
```

## Flags

Command | Detail
:-- | --:
-host, --host | Specify the host
-k, --key | Unique api key
-f, --file | Specify file location to be scanned
-w, --workflow | active workflows, allowed values: mcl-metadefender-rest-sanitize-disabled-unarchive
-p, --p | password for password protected files
 


## Author

Limi Hodory
