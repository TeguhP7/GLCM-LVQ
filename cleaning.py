import cv2 as cv
import os

face_cascade = cv.CascadeClassifier(
    'E:/Project/Deteksi_masker/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('E:/Project/Deteksi_masker/haarcascade_eye.xml')
nose_cascade = cv.CascadeClassifier('E:/Project/Deteksi_masker/Nariz_Hidung.xml')


def cleaning(dir_name='E:/Project/Deteksi_Masker_Project/dataset/test'):
    folder_hasil = 'E:/Project/Deteksi_Masker_Project/dataset/test'
    i=1
    for namafile in os.listdir(dir_name):
        if os.path.isfile(dir_name+'/'+namafile):
            img = cv.imread(dir_name+'/'+namafile, 1)
            # deteksi wajah
            face = face_cascade.detectMultiScale(img, 1.1, 3)
            # print(face)
            # for i in range (len(os.listdir(dir_name))):
            for (x, y, w, h) in face:
                roi = img[y:y+h, x:x+w]
                file = 'test'+str(i)+'.jpg'
                cv.imwrite(folder_hasil+'/'+file, img=roi)
        i+=1

if __name__ == '__main__':
   cleaning()

   