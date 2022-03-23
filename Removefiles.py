from operator import truediv
import os
import shutil
from sys import path_hooks
import time

path = input("Enter the name of the directory to remove: ")
d = input("Enter the number of days: ")
days = time.time()
isExist = os.path.exists(path)

if isExist:
    for root, dirs, files in os.walk(path, topdown=False):
     for name in files:
      fname=os.path.join(root, name)
      ctime=os.stat(fname).st_ctime
      print(ctime)
      if ctime > days:
          os.remove(fname)
      else:
          shutil.rmtree(path)
else:
    print("Path does not exist")         

print(isExist)
print(days)
