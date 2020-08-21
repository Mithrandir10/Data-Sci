import os
import string
import random
import time

os.chdir("D://Data Sci//text")

l=[]

for i in string.ascii_letters:
    l.append(i)
print(l)

for i in range(500):
    f=open(f"{i}.txt","w+")
    for k in range(20000):
      if k!=0:
       f.write("\n")
      for j in range(20):
        f.write(random.choice(l))

f2=open("data.csv","w+")
t4=0
for i in range(500):
    t1=time.perf_counter_ns()
    f1=open(f"{i}.txt","r+")
    k=f1.readlines()
    f1=open(f"{i}.txt","w")
    for j in k:
        f1.write(j.upper())
    t2=time.perf_counter_ns()
    t3=t2-t1
    t4=t4+t3
    f2.write(f"{t3}")
    f2.write("\n")
print(t4)