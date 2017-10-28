import os,sys,time
import adboperations as adb
import anim

directory="/home/suzan/Desktop/apks"
installed=[]
failed=[]


def main():
	print("Checking if adb is installed or not")
	if adb.exist():
		print(" ADB is Installed..")
	else:
		print(" ADB is not found..")
		kill()

def kill():
	print("\n\n[Installed:{x},Failed:{y} and Processed:{}]".format(x=len(installed),y=len(failed),len(installed)+len(failed)))
	print("Exiting..")
	exit()


if __name__ == '__main__':
	main()
	kill()
