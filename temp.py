import os
import time

os.chdir("D://Data Sci//text")
"""
for i in range(500):
    f=open(f"{i}.txt","r")
"""
for i in range(500):
 f=open(f"{i}.txt","r")
 p=f.read()
 st="RE"
 y=p.find(st)
 if y!=-1:
  print(f"\nWord found in file {i}.txt")
  for x in range(len(st)):
    print(p[y+x])