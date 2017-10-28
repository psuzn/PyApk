import subprocess as sp
import itertools,time,sys,os
maxCharacter=os.get_terminal_size().columns
bannerart=\
"""	
    /$$$$$$$             /$$$$$$            /$$      
   | $$__  $$           /$$__  $$          | $$      
   | $$  \ $$ /$$   /$$| $$  \ $$  /$$$$$$ | $$   /$$
   | $$$$$$$/| $$  | $$| $$$$$$$$ /$$__  $$| $$  /$$/
   | $$____/ | $$  | $$| $$__  $$| $$  \ $$| $$$$$$/ 
   | $$      | $$  | $$| $$  | $$| $$  | $$| $$_  $$ 
   | $$      |  $$$$$$$| $$  | $$| $$$$$$$/| $$ \  $$
   |__/       \____  $$|__/  |__/| $$____/ |__/  \__/
             /$$  | $$          | $$                
            |  $$$$$$/          | $$                
             \______/           |__/        [by suzn]


                         
"""

def showBanner():
	for line in bannerart.splitlines():
		for i in range(0,len(line)):
			sys.stdout.write(line[i])
			sys.stdout.flush()
			if not line[i]==" ":
				time.sleep(0.005)
		sys.stdout.write("\n")



def anim(text):
	spinner=itertools.cycle(["|","/","-","\\","|"])
	while True:
		sys.stdout.write("{}....{}".format(text,next(spinner)))
		sys.stdout.flush()
		sys.stdout.write('\b'*(len(text)+5) )
		time.sleep(0.1)
		continue

def cleanup(textToclean,newText=None):
	if newText==None:
		newText=textToclean

	sys.stdout.write('\b'*(len(textToclean)+5) )
	for lines in newText.splitlines():
		sys.stdout.write("{}{}\n".format(lines," "*(maxCharacter-len(lines))))
	

def animate(text):
	return sp.Popen(["python3","anim.py","anim" ,text])

def clean(text):
	 process=sp.Popen(["python3","anim.py","cleanup",text])
	 while process.poll()==None:
	 	time.sleep(0.1)

if __name__ == '__main__':
	if  "anim" in sys.argv[1:]:
		anim("".join(sys.argv[2:]))

	elif "cleanup" in sys.argv[1:]:
		cleanup("".join(sys.argv[2:]))

