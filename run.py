#!/usr/bin/python3

#AUTOMATION SCRIPT TO OPEN UP FAVORITE APPS AND WEBSITES IN ONE GO...

import webbrowser
import subprocess
print("Hello ...")
y = input("Start Browser Now..?y/n :")
if(y=='y'):
    webbrowser.get('firefox').open_new_tab('http://www.google.com')#Change Links To Target Required Websites...
    webbrowser.get('firefox').open_new_tab('https://github.com/login')#".get" Can Be Avoided If You Wish To Open default Browser
subprocess.call("gnome-terminal")
subprocess.call("nautilus")
subprocess.call("code /home/ank/VScode/Untitiled-1",shell=True)