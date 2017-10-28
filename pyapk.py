import os,sys,time
import adboperations as adb

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

if __name__ == '__main__':
	main()
