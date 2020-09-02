import os
"""
os.chdir("D://pro")

for a,b,c in os.walk("D:\pro"):
        for j in c:
            d=os.path.join(a,j)
            os.remove(d)
"""

parent=os.getcwd()
new="Frames"
dirpath=os.path.join(parent,new)
os.rmdir(dirpath)
newconv="ConvFrames"
dirpathconv=os.path.join(parent,newconv)
os.rmdir(dirpathconv)