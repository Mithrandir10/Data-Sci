import cv2
import glob
import os
v_name=input("Enter the name of the video (with format) :")
vid = cv2.VideoCapture(f'D://{v_name}')
fps=vid.get(cv2.CAP_PROP_FPS)
print(fps)
check,image = vid.read()
count = 0
while check:
  cv2.imwrite("D://pro//frame%d.jpg" % count, image)   
  check,image = vid.read()
  print('Read a new frame: ', check)
  count += 1

t=0
while(t<count):
 img=cv2.imread(f"D:/pro/frame{t}.jpg",0)
 cv2.imwrite(f"D:/pro/Conv/{t}.jpg",img)
 t=t+1


vimages=[]
img=glob.glob("D:\pro\conv\*.jpg")
def srtcrt(a):
  return(int(a[12:-4]))
img.sort(key=srtcrt)
for i in img:
  print(i)

  

for i in img:
    img1=cv2.imread(i)
    h,w,layers=img1.shape
    size=(w,h)
    vimages.append(img1)
    
v_name=input("Enter the name of the converted video (without format) : ")
vid=cv2.VideoWriter(f'D:/{v_name}.mp4',cv2.VideoWriter_fourcc(*'mp4v'),fps,size)


for i in range(len(vimages)):
    vid.write(vimages[i])
vid.release()