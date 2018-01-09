# PyApk
It's a CLI program(basically a script) to install apks on a directory(including apks in sub-directory of it) on your pc to android phone using Android Debugging Bridge(ADB) interface.

When you prefer to backup only /data/app/ directory for the applications  rather than entire /data/ partition,it is real pain to install all the apks(50+ in my case) manually.

I was thinking about creating my own version of inline console animation and also try the subprocess module of python long before. So I decide to try both of those in in this program.

[![Demo](https://i.imgur.com/oLAYN2M.gif)]

**Inside it:**
- The animation on it is in the separate child-process .
- Nice console log output (at least for me).
- It installs all the apks in a directory including apks on sub-directory (ofcourse it does).



**Way to use it:**

If you decide to give it a try than  put your folder containing apks inside 'apk'   folder on the same directory as the script :

PyApk/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--pyapk.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--adboperations.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--anim.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--apks/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--apk1.apk<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--apk2.apk


And just execute it  (dont forget to connect your phone with adb enabled)

```
$ ./pyapk.py
```
OR
```
$ python3 pyapk.py
```

If you don't like this way  you can also provide the fullpath of your apk folder as CLI argument:

```
$ ./pyapk.py /absolute/path/to/folder/
```
