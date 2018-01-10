import subprocess as sp
import sys,time,os
from pyapk import anim
maxCharacter=os.get_terminal_size().columns

def exist():
	if 'version'  in sp.run(['adb'],stdout=sp.PIPE,stderr=sp.PIPE,encoding='utf-8').stdout:
		
		return True
	else:
		
		return False

def checkdevice(echo=True):
	process=sp.Popen(["adb","devices"],stdout=sp.PIPE,stderr=sp.PIPE,encoding='utf-8')
	animText="Checking if device with adb enable is connected or not....";
	animProcess= anim.animate(animText) if echo else False

	while process.poll()==None:
		time.sleep(0.2)
		continue
	if echo:
		animProcess.terminate()
		anim.clean(animText)

	data=process.communicate()[0]
	data=data.splitlines()
	if "device" in data[1]:
		return (True,data[1].replace("\n"," "))
	else:
		return (False,None)

def install(absolutepath,name,count):
	process=sp.Popen(["adb","install","{}".format(absolutepath)],stdout=sp.PIPE,stderr=sp.PIPE,encoding='utf-8')
	#process=sp.Popen(["ping","localhost","-c 5"],stdout=sp.PIPE,stderr=sp.PIPE,encoding='utf-8')
	animText="[{}]Installing..".format(count)
	animProcess= anim.animate(animText)
	while process.poll()==None:
		time.sleep(0.2)
		continue
	animProcess.terminate()
	anim.clean(animText)
	data,error=process.communicate()
	if "Success" in data or "Success" in error:
		return (True,True)
	else:
		return (False,error)