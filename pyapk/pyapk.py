#!/bin/python3
import os,sys,time
from pyapk import adboperations as adb
from pyapk import anim


directory=''
installed=[]
failed=[]
maxCharacter=os.get_terminal_size().columns

def cursorUp(up):
	CURSOR_UP='\033[F'
	print(CURSOR_UP*(up+1))
	print((" "*maxCharacter+"\n")*(up))
	print(CURSOR_UP*(up+2))
def max(name,length=None,extension=""):
	if not length:
		length = maxCharacter
	return name[:length-5]+".."+extension if len(name)> length else name

def printLog(previoussuccess,previousfailed):
	cursorUpLines=3
	if not previoussuccess == 0:
		cursorUpLines+=1+previoussuccess+1
	if not previousfailed == 0:
		cursorUpLines+=1+previousfailed*2+1
	cursorUp(cursorUpLines)
	if len(installed) >0:
		print("\n[Installed]")
		index=0
		for name in installed:
			index+=1
			print(" [{}]{}".format(index,max(name=name,length=maxCharacter-5,extension="apk")))
	if len(failed) >0:
		index=0
		print("\n[Failed]")
		for name,error in failed:
			index+=1
			print(" [{}]{}\n   {}{}".format(index,max(name=name,length=maxCharacter-5,extension="apk"),chr(187),max(name=error,length=maxCharacter-5)))
def waitForDevice():
	animProcess= anim.animate("Device is Disconnected waiting..")
	status,device=adb.checkdevice(echo=False)
	while not status:
		time.sleep(0.2)
		status,device=adb.checkdevice(echo=False)
		continue
	animProcess.terminate()
	anim.cleanup("Device found\n{}".format(device.replace("\n","")))
	animProcess= anim.animate("Resuming installation..")
	time.sleep(2)
	animProcess.terminate()
	anim.cleanup("Resumed..\n{}".format(device.replace("\n","")))
	time.sleep(0.2)
	cursorUp(6)


def install(root,name):
	absolutepath=os.path.join(root,name)
	print( "\nFound apk file #{}[{:.3f}MB]".format(max(name=name,length=maxCharacter-35,extension="apk"),os.path.getsize(absolutepath)/1048576 ))
	status,data=adb.install(absolutepath=absolutepath,name=name,count=len(installed)+len(failed)+1)
	if status:
		installed.append(name)
		printLog(previoussuccess=len(installed)-1,previousfailed=len(failed))
	else:
		if "Failure" in data:
			error=data.split("Failure")[1]
			error=error.split(": ")[0]+"]" if ": " in error else error
		elif not adb.checkdevice(echo=False)[0]:
			error="[Device disconnected]"
		else:
			error="[Unknown error]"

		failed.append((name,error.replace("\n"," ")))
		printLog(previoussuccess=len(installed),previousfailed=len(failed)-1)


def main():
	global directory
	anim.showBanner()
	if '-c' in sys.argv[1:]:
		directory=os.getcwd()
	elif '-d' in sys.argv[1:]:
		directory=sys.argv[2]
	else:
		return

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
	print("Installing apks on directory '{}'".format(directory))

	for root,dirs,files in os.walk(directory):
		for name in files:
			if name.endswith(".apk"):
				if not adb.checkdevice(echo=False)[0]:
					waitForDevice()
				install(name=name,root=root)


def kill():

	print("\n\t\t[Installed:{},Failed:{} and Processed:{}]".format(len(installed),len(failed),len(installed)+len(failed)))
	if len(installed)==0 and len(failed)==0:
		print("\t\t  The directory provided seems empty")
	print("Exiting..")
	exit()

def pyapkInit():
	if  "anim" in sys.argv[1:]:
		anim.anim("".join(sys.argv[2:]))
	elif "cleanup" in sys.argv[1:]:
		anim.cleanup("".join(sys.argv[2:]))
	else:
		main()
		kill()
