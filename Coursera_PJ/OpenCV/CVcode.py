import zipfile
import os
from PIL import Image
import pytesseract as pt
import cv2 as cv
import numpy as np


def faceparser(word, folder):
    for tup in img_lst:
        if word in tup[1]:
            print('Results found in file {}'.format(tup[0]))
            try:
                image = Image.open(folder+tup[0])
                faces = (face_cascade.detectMultiScale(np.array(image),1.35,4)).tolist()
                faces_lst = list()
                
                for x, y, z, h in faces:
                    faces_lst.append(image.crop((x, y, z+x, y+h)))
                # display((img.crop((x,y,x+z,y+h))).resize((110,110)))
                contact_sheet = Image.new(image.mode, (550, 110*int(np.ceil(len(faces_lst)/5))))
                x, y = 0, 0
                
                for face in faces_lst:
                    face.thumbnail((110,110)) # resize current image(face)
                    contact_sheet.paste(face, (x, y))
                    if x + 110 == contact_sheet.width: x, y = 0, y + 110
                    else: x += 110
                        
                display(contact_sheet)
                
            except Exception as e:
                print(e)
                print('There were no faces in file!')
                
# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!

zip_1 = zipfile.ZipFile('readonly/small_img.zip', 'r')
zip_1.extractall('small_img')
zip_1.close()

zip_1 = zipfile.ZipFile('readonly/images.zip', 'r')
zip_1.extractall('images')
zip_1.close()

# for the 'small_img' folder
img_lst = []
imgs = os.listdir('small_img')
for img in imgs:
    image = Image.open('small_img/'+img)
    img_lst.append((img, pt.image_to_string(image).replace('-\n','')))

faceparser("Christopher",'small_img/')

# for the 'images' folder
img_lst = []
imgs = os.listdir('images')

for img in imgs:
    image = Image.open('images/'+img)
    img_lst.append((img, pt.image_to_string(image).replace('-\n','')))

faceparser("Mark", 'images/')