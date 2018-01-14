# PyApk

Small python program to install all apks on a directory(including apks in sub-directory of it) in your pc to android phones.

When you prefer to backup only /data/app/ directory for the applications  rather than entire /data/ partition,it is real pain to install all the apks(50+ in my case) manually.

I was thinking about creating my own version of inline console animation and also try the subprocess module of python long before. So I decide to try both of those in in this program.

[![Demo](https://i.imgur.com/oLAYN2M.gif)](https://github.com/psuzn/PyApk)

**Inside it:**
- Separate child-process animation .
- Nice console log output (at least for me).
- It installs all the apks in a directory including apks on sub-directory (of course it does).


**Way to install it:**
- Install [adb](https://www.xda-developers.com/install-adb-windows-macos-linux/) on your pc.
- install pyapk with pip:
```
	$ pip install pyapk
```
OR 
- install with python setup.py
```
$ git clone https://github.com/psuzn/PyApk.git
$ cd PyApk && sudo python setup.py install
```

**How to use it:**

cd into the directory containing apks  and 
```
$ pyapk -c
```
OR

Just provide path of apks containing directory
```
$ pyapk -d /path/to/apks/
```


**(And dont forget to connect your phone and [enable]((https://www.xda-developers.com/install-adb-windows-macos-linux/)) adb from developer option)**



