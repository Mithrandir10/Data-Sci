import cv2
import glob

vimages=[]

for i in glob.glob('D:/pro/Conv/*.jpg'):
    img=cv2.imread(i)
    h,w,layers=img.shape
    size=(w,h)
    vimages.append(img)

vid=cv2.VideoWriter('D:/barca.mp4',cv2.VideoWriter_fourcc(*'mp4v'),30,size)

for i in range(len(vimages)):
    vid.write(vimages[i])
vid.release()