import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import xlsxwriter as xls
from skimage.feature import graycomatrix, graycoprops
import math
import os
import pandas as pd


class Fungsi:
    def preprocessing(gambar):
        h, w = gambar.shape[:2]
        max_height = 240
        max_width = 240
        if max_height <= h or max_width <= w:
            # get scaling factor
            scaling_factor = max_height / float(h)
            if max_width/float(w) < scaling_factor:
                scaling_factor = max_width / float(w)
            # resize image
            gambar = cv.resize(gambar, None, fx=scaling_factor,
                               fy=scaling_factor, interpolation=cv.INTER_AREA)
        elif max_height > h or max_width > w:
            scaling_factor = max_height / float(h)
            # resize image
            gambar = cv.resize(gambar, None, fx=scaling_factor,
                               fy=scaling_factor, interpolation=cv.INTER_AREA)

        gambar = cv.cvtColor(gambar, cv.COLOR_BGR2GRAY)
        return gambar

    def load(dir_name='E:/Project/Deteksi_Masker_Project/dataset/dataset_hasil/without_mask'):
        gambar = []
        for namafile in os.listdir(dir_name):
            if os.path.isfile(dir_name+'/'+namafile):
                img = cv.imread(dir_name+'/'+namafile, 1)
                gambar.append(img)
        return gambar

    def ekstraksi(gambar):
        # Fitur GLCM
        fitur_glcm = ['correlation', 'homogeneity',
                      'dissimilarity', 'contrast', 'energy', 'ASM']
        jarak = [1]
        sudut = [0, np.pi/4, np.pi/2, 3*np.pi/4]
        fungsi_glcm = graycomatrix(
            gambar, jarak, sudut, 256, True, True)
        glcm_props = [propery for name in fitur_glcm for propery in graycoprops(
            fungsi_glcm, name)[0]]
        return glcm_props


def run():
    book = xls.Workbook('E:/Project/Deteksi_Masker_Project/dataset/dataset_hasil/without_mask.xlsx')
    sheet = book.add_worksheet()
    sheet.write(0, 0, 'Nama File')
    col = 1

    fitur_glcm = ['correlation', 'homogeneity',
                  'dissimilarity', 'contrast', 'energy', 'ASM']
    sudut = ['0', '45', '90', '135']
    for i in fitur_glcm:
        for j in sudut:
            sheet.write(0, col, i+'_'+j)
            col += 1

    row = 1
    imgs = Fungsi.load()
    dir_name = 'E:/Project/Deteksi_Masker_Project/dataset/dataset_hasil/without_mask'

    for namafile in os.listdir(dir_name):
        if os.path.isfile(dir_name+'/'+namafile):
            col = 0
            # nama_file = i + '_' + str(j) + '.jpg'
            # print(namafile)
            sheet.write(row, col, namafile)
            row += 1

    row = 1
    for img_is in imgs:
        col = 1
        img_is = Fungsi.preprocessing(img_is)
        hasil_ekstraksi = Fungsi.ekstraksi(img_is)

        for item in hasil_ekstraksi:
            sheet.write(row, col, item)
            col += 1

        row += 1
    book.close()
    
if __name__ == "__main__":
    run()
