from os import system
from os import getcwd
import json
from time import time
return_text=system("git pull |grep cmd.json")
if (return_text==256):
    print ("no new cmd")
else:
    cmd_f=open("cmd.json","r")
    cmd_json=json.load(cmd_f)
    cmd=cmd_json["cmd"]
    if(cmd=="take-a-pic"):
        print("take a pic")
        system("fswebcam -d /dev/video0 %s/pics/%s.jpg" % (getcwd(),int(time())))
        system("%s/push.sh" % (getcwd()))
    if(cmd=="turn-on-light"):
        print("turn on light")
    if(cmd=="turn-off-light"):
        print("turn off light")
    print(cmd)
