import image_slicer
import os
import glob
import Image
import pytesseract
from multiprocessing import Pool

def result(name):
    #print Pool.current_process()
    #print "process id = " , os.getpid()
    os.system("python process_image.py "+name+" text"+str(os.getpid())+".jpg")
    #print pytesseract.image_to_string(Image.open('text'+str(os.getpid())+'.jpg'))
    #text_file = open("Output"+str(os.getpid())+".txt", "w")
    #text_file.write("for"+str(os.getpid())+": %s" % pytesseract.image_to_string(Image.open('text'+str(os.getpid())+'.jpg')))
    #text_file.close()
pool = Pool(processes=4)
no=input("no of slices :")
image_slicer.slice('test.jpg',no)
list=glob.glob("*.png")
print(list)

#for a in list:
pool.map(result,list)
    
list2=glob.glob("*.jpg")
list2.pop(0)
for a in list2:
    print pytesseract.image_to_string(Image.open(a))
