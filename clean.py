import os

os.chdir("D://pro")

for a,b,c in os.walk("D:\pro"):
        for j in c:
            d=os.path.join(a,j)
            os.remove(d)