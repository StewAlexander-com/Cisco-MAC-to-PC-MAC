#!/usr/bin/env python3
import os
import sys
import time

#if mac_address_TEMP1.txt exists, delete it
if os.path.exists("mac_address_TEMP1.txt"):
    os.remove("mac_address_TEMP1.txt")

#if mac_address_TEMP2.txt exists, delete it
if os.path.exists("mac_address_TEMP2.txt"):
    os.remove("mac_address_TEMP2.txt")

#if "MAC_Address_PC.txt" exists, delete it
if os.path.exists("MAC_Address_PC.txt"):
    os.remove("MAC_Address_PC.txt")

#Print an opening to the program
print("\n\nThis program will convert MAC addresses from Cisco format\nto PC format and will enter the MAC addresses into a text file called\n>" "\"MAC_Address_PC.txt\" \n")

#Print this requires a list of MAC addresses from a cisco switch to be in a file
print("""This program requires a list of MAC addresses from a Cisco switch\nto be in a file in the same directory as the program \n\n""")

#open a path to the current directory
path = os.path.dirname(os.path.realpath(__file__))
#show the contents of the curent directory
print ("The current directory is:\n\"" + path, "\", and the list of contents is:")
print(os.listdir())
#ask the user to enter the yaml file name
MAC_file = input("\nPlease enter the MAC Address file name: ")

# while loop to check if the file exists
while True:
    if os.path.isfile(MAC_file):
        print ("Ingesting the file\n")
        break
    else:
        print("File does not exist")
        MAC_file = input("Please enter the MAC Address file name: ")

#open the file and read the contents
print("Creating TEMP file #1\n")
with open(MAC_file, 'r') as f:
    MAC_list = f.readlines()
    #take every line and make it uppercase
    for line in MAC_list:
        line = line.upper()
        #save "line" to a new file name mac_address_TEMP1.txt
        with open("mac_address_TEMP1.txt", 'a') as f:
            f.write(line)

#Close the file mac_address_TEMP1.txt
f.close()

#Close the MAC_file
f.close()

#Open the file mac_address_TEMP1.txt and read the contents
print ("Creating TEMP file #2\n")
with open("mac_address_TEMP1.txt", 'r') as f:
    MAC_list = f.readlines()
   #take every cisco formatted mac address and make it a PC formatted mac address
    for line in MAC_list:
      #remove any "." from every line
        line = line.replace(".", "")
      #Add a : to every 2nd character
        line = line[0:2] + ":" + line[2:4] + ":" + line[4:6] + ":" + line[6:8] + ":" + line[8:10] + ":" + line[10:12]
        #add a new line the end of every line in the file
        line = line + "\n"
        #save "line" to a new file named mac_address_PC.txt
        with open("MAC_Address_TEMP2.txt", 'a') as f:
            f.write(line)

#Close the file mac_address_TEMP1.txt
f.close()

#Close the file MAC_address_TEMP2.txt
f.close()

#Remove empty lines from the file MAC_Address_PC.txt
print ("Creating \"MAC_Address_PC.txt\"\n")
with open("MAC_Address_TEMP2.txt", 'r') as f:
    MAC_list = f.readlines()
    #remove empty lines
    for line in MAC_list:
        if line == "\n":
            MAC_list.remove(line)
    #save the new file to MAC_Address_PC.txt
    with open("MAC_Address_PC.txt", 'w') as f:
        f.writelines(MAC_list)

#Close the file mac_address_TEMP2.txt
f.close()

#Close the file MAC_Address_PC.txt
f.close()

#Telling the user to open the file MAC_Address_PC.txt to see the results
print("Please open the file \"MAC_Address_PC.txt\"\nin \""+ path + "\" to see the results")

#Press return to quit
quit = input("\nPress return to quit")
time.sleep(0.7)
sys.exit()