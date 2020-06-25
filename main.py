import os
import hashlib
import sys
import socket
import json
import requests

# Options avalible
print("Please type what you want to do as the option number")
print("1: Generate and compair an MD5 hash to a file")
print("2: Preform a reverse DNS lookup fo a given IP address")
print("3. Preform a port scan on ports 20, 22, 23, 80 and 445")
print("4. Return the geo location of a given IP address")

menu_choise = int(input("Please input your choise as just the option number: "))


# Menu choise 1
# compair md5 sums
if menu_choise == 1:
  # show files in current working dir
  print("The files in this directory are: ")
  for file in os.walk("."):
    print(file)
  # Take users choise for a file and ask again if it can't be found
  chk = False
  while chk == False:
    md5_file = input("What file would you like the programm to run on?:  ")
    chk = os.path.isfile(md5_file)
  
  md5_sum = input("What is the md5 sum the file should have: ")
  # Generate a MD5 sum from the file
  with open(md5_file) as file_to_check:
    data = file_to_check.read()
    md5_returned = hashlib.md5((data).encode('utf-8')).hexdigest()
  # Check that the hashes match each other
  if md5_sum == md5_returned:
    print("The MD5 sum matchs.")
  else:
    print("The MD5 sum does not match the given one.")



# menu option 2
# reverse DNS lookup for a given IP address.
if menu_choise == 2:
  # Take and check that the user input is an IP address
  chek = False
  while chek == False:
    ip = input("What is the IP you want to look up: ")
    parts = ip.split(".")
    if len(parts) == 4 and all(map(lambda x: int(x)<256, parts)):
     chek = True
  # Run through each port and scan it under the adress given
  try :
    result=socket.gethostbyaddr(ip)
    print ("The host name is: ")
    print (" "+result[0])
    print ("From IP address: ")
    for item in result[2]:
        print (" "+item)
  except:
    print ("error for resolving ip address. It's either closed or dead")


# menu option 3
# Open port scan 
if menu_choise == 3:
  # Take and check that the user input is an IP address
  check = False
  while check == False:
    ip = input("What is the IP you want to look up: ")
    parts = ip.split(".")
    if len(parts) == 4 and all(map(lambda x: int(x)<256, parts)):
     check = True
  # take the ip address then check a port from the array  to see if it returnes anything.
  print("This may take a while. Ports 20, 22, 23, 80 and 445 will be scanned.\nThe open ports are: \n")
  portlist = [20,22,23,80,445]
  for port in portlist:
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((ip,port))
    print (str(port) + ":" + str(result))
    sock.close()


# Menu choise 4
# Return geolocation of a given ip address
if menu_choise == 4:
  # Take and check that the user input is an IP address
  check = False
  while check == False:
    ip = input("What is the IP address you want to geo locate: ")
    parts = ip.split(".")
    if len(parts) == 4 and all(map(lambda x: int(x)<256, parts)):
     check = True
  # preform a json request and print the data that is returned
  try:
    json_request = requests.get('http://api.hostip.info/get_json.php?ip=%s&position=true' % ip).json()
    country = json_request['country_name']
    country_code = json_request['country_code']
    city = json_request['city']
    print (socket.gethostbyaddr(ip))
    print (country + ":" + city)
  except:
    print ("Host not found")

  try:
    request = requests.get("https://api.hackertarget.com/geoip/?q=141.101.20.110")
    print (request.text)
  except:
    print ("not working")
