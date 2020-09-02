import cv2
import sys
import glob
import os
import shutil

if (len(sys.argv)!=3):
  print("\nInsufficient Arguments")
  sys.exit()
parent=os.getcwd()
new="Frames"
dirpath=os.path.join(parent,new)
os.mkdir(dirpath)
newconv="ConvFrames"
dirpathconv=os.path.join(parent,newconv)
os.mkdir(dirpathconv)
print(dirpathconv)
v_name=sys.argv[1]
vid = cv2.VideoCapture(f'{v_name}')
fps=vid.get(cv2.CAP_PROP_FPS)
print(fps)

check,image = vid.read()
count = 0
while check:
  cv2.imwrite(f"{dirpath}/frame{count}.jpg", image)   
  check,image = vid.read()
  print(f'Frame number {count}: {check}')
  count += 1
print("\nPlease Wait!!")
t=0
try:
 prc=100-int(sys.argv[2])
except:
  print("\n Insufficient Arguments : Resize Value not provided")
  sys.exit()
while(t<count):
 img=cv2.imread(f"{dirpath}/frame{t}.jpg",cv2.IMREAD_UNCHANGED)
 hnew=int(img.shape[0]*(prc/100))
 wnew=int(img.shape[1]*(prc/100))
 snew=(wnew,hnew)
 nimg=cv2.resize(img,snew)
 cv2.imwrite(f"{dirpathconv}/Conv{t}.jpg",nimg)
 t=t+1

vimages=[]
img=glob.glob(f"{dirpathconv}/*.jpg")
def srtcrt(a):
   x=len(dirpathconv)
   return(int(a[(x+5):-4]))
img.sort(key=srtcrt)
for i in img:
  print(i)

  

for i in img:
    img1=cv2.imread(i)
    h,w,layers=img1.shape
    size=(w,h)
    vimages.append(img1)

    
v_name='vid_output'
try:
 vid=cv2.VideoWriter(f'{parent}/{v_name}.mp4',cv2.VideoWriter_fourcc(*'mp4v'),fps,size)
except:
  print("File not found")
  os.rmdir(dirpath)
  os.rmdir(dirpathconv)
  sys.exit()

for i in range(len(vimages)):
    vid.write(vimages[i])
vid.release()
shutil.rmtree(dirpath)
shutil.rmtree(dirpathconv)
print("DONE")
print(f"OUTPUT : {v_name}")