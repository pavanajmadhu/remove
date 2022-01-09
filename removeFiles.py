import os
import shutil
import time

path=input("the folder  : ")
days=time.ctime(os.path.getmtime(path))

path=path+"/"
days=days.time.time()

if os.path.exists(path):
    os.walk(path)
else:
    print("folder not found")

ctime=os.stat(path).st_ctime

if days>30:
    os.remove(path)







