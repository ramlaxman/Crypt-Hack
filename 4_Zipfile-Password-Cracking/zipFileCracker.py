'''
Title: ZipFile Password Cracking using Dictionary based Attack
Author: Qaidjohar Jawadwala
For Educational Purpose Only

Status: Working
Usage: python zipFileCracker.py
'''

import zipfile

#Selecting ZipFile
zipF = zipfile.ZipFile("sample_enc.zip")
dictFilename = raw_input("Enter Dictionary File Name: ")
dictPtr = open(dictFilename,'r')

for d in dictPtr.readlines():
	val = d.strip('\n')
	try:
		zipF.extractall(pwd=val)
		print("------------------------------------------")
		print("\tValid Password is "+val)
		print("------------------------------------------")
		break
	except:
		print("[-] Invalid Password: "+val+"\r")

