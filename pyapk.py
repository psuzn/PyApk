import os,sys,time
import adboperations as adb
import anim

directory="/home/suzan/Desktop/apks"
installed=[]
failed=[]


def main():
	print("Checking if adb is installed or not")
	if adb.exist():#Adb installation check
		print(" ADB is Installed..")
	else:
		print(" ADB is not found..")
		kill()
	status,device=adb.checkdevice()
	if status:#device check
		print(" Found a device\n {} \n".format(device))#show device's host id
	else:
		print(" No device with ADB enabled found")
		kill()	
	


def kill():
	print("\n\n[Installed:{},Failed:{} and Processed:{}]".format(len(installed),len(failed),len(installed)+len(failed)))
	print("Exiting..")
	exit()


if __name__ == '__main__':
	main()
	kill()
