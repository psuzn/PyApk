import subprocess as sp
import sys,time

def exist():
	if 'version'  in sp.run(['adb'],stdout=sp.PIPE,stderr=sp.PIPE,encoding='utf-8').stdout:
		
		return True
	else:
		
		return False
