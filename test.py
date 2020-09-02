import os 
import glob 
import sys
import shutil
parent=os.getcwd()
"""

new="Frames"
dirpath=os.path.join(parent,new)
shutil.rmtree(dirpath)
newconv="ConvFrames"
dirpathconv=os.path.join(parent,newconv)
shutil.rmtree(dirpathconv)
"""

os.remove(f"{parent}/vid_output.mp4")