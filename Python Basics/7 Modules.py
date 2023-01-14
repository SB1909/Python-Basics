'''
#time modue:
import time
dir(time)
print("Hello SB")
time.sleep(2)
print("LnB")
'''
'''
from time import sleep
count=0
while count<10:
    count=count+1
    sleep(2)
    print("Hey")
    sleep(1)
    print("LnB")
'''

'''
#os module:
import os
for i in dir(os):
    if 'sys' in i:
        print(i)
print([i for i in dir(os) if 'sys' in i]) #OR in a list form
os.system('uname')
os.system('notepad')
'''

'''
#subprocess
import subprocess
subprocess.getstatusoutput('date') #check it aagain
'''

import emoji
print(emoji.emojize(":thumbs_up:"))
print(emoji.emojize(":zipper-mouth_face:"))
