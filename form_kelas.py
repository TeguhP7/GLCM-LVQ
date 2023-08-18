from PyQt5 import QtCore, QtGui, QtWidgets
import glcm_fitur
import numpy as np
import cv2 as cv
import os
import pandas as pd


class Ui_form_kelas(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_form_kelas, self).__init__()
        self.setObjectName("form_kelas")
        self.resize(330, 207)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "E:/Project/Deteksi_Masker_Project/assets/icons/mask.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet(
            "QDialog#form_kelas{background-image:url(E:/Project/Deteksi_Masker_Project/assets/wallpapers/bg3.jpg)}")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(45, 30, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Humnst777 BlkCn BT")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 251, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_memakai = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_memakai.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_memakai.setStyleSheet("background-color:cyan")
        self.btn_memakai.setCheckable(False)
        self.btn_memakai.setDefault(False)
        self.btn_memakai.setObjectName("btn_memakai")
        self.btn_memakai.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.btn_memakai)
        self.btn_memakai.clicked.connect(self.kls_memakai)

        self.btn_tidak_memakai = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_tidak_memakai.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_tidak_memakai.setStyleSheet(
            "background-color:cyan")
        self.btn_tidak_memakai.setCheckable(False)
        self.btn_tidak_memakai.setDefault(False)
        self.btn_tidak_memakai.setObjectName("btn_tidak_memakai")
        self.btn_tidak_memakai.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.btn_tidak_memakai)
        self.btn_tidak_memakai.clicked.connect(self.kls_tidak_memakai)

        self.lbl_memakai = QtWidgets.QLabel(self)
        self.lbl_memakai.setGeometry(QtCore.QRect(300, 77, 16, 16))
        self.lbl_memakai.setText("")
        self.lbl_memakai.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_memakai.setObjectName("lbl_memakai")
        self.lbl_tdk_memakai = QtWidgets.QLabel(self)
        self.lbl_tdk_memakai.setGeometry(QtCore.QRect(300, 118, 16, 16))
        self.lbl_tdk_memakai.setText("")
        self.lbl_tdk_memakai.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tdk_memakai.setObjectName("lbl_tdk_memakai")

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(87, 160, 156, 23))
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.final)
        self.buttonBox.rejected.connect(self.close)

        self.lbl_peringatan = QtWidgets.QLabel(self)
        self.lbl_peringatan.setGeometry(QtCore.QRect(0, 184, 331, 20))
        self.lbl_peringatan.setStyleSheet("color:red;")
        self.lbl_peringatan.setText("")
        self.lbl_peringatan.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_peringatan.setObjectName("lbl_peringatan")
        ################################
        # variabel
        ################################
        fitur_glcm = ['correlation', 'homogeneity',
                      'dissimilarity', 'contrast', 'energy', 'ASM']
        arah_sudut = ['0', '45', '90', '135']
        self.keys = ['Nama File', ]
        for fitur in fitur_glcm:
            for sudut in arah_sudut:
                key = fitur+'_'+sudut
                self.keys.append(key)
        self.keys.append('Class')

        self.dataset = []
        #################################

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def load(self):
        dir = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select Image File',
                                                     filter="All (*);;JPEG (*.jpg);;PNG(*.png)")
        self.gambar = []
        self.nama_file = []
        for namafile in dir[0]:
            self.image = namafile
            # self.f_type = os.path.splitext(namafile)
            (self.directory, self.filename) = os.path.split(self.image)
            self.nama_file.append(self.filename)
            self.raw_data = np.array(cv.imread(
                self.image))
            self.gambar.append(self.raw_data)
        self.glcm()

    def glcm(self):
        modul = glcm_fitur.Fungsi
        self.hasil_ekstraksi = []
        for data in self.gambar:
            preprocessing_img = modul.preprocessing(data)
            self.data = modul.ekstraksi(preprocessing_img)
            self.hasil_ekstraksi.append(self.data)
        # print('glcm', self.hasil_ekstraksi)
        return self.hasil_ekstraksi

    def kls_memakai(self):
        self.load()
        kelas = ['Memakai']
        for nama, ekstrak in zip(self.nama_file, self.hasil_ekstraksi):
            nama = [nama]
            hasil = nama + ekstrak + kelas
            self.dataset.append(hasil)

        # with open('E:/Project/Deteksi_Masker_Project/dataset/dataset.csv', 'a', newline='\n') as dataset_csv:
        #     dataset = csv.DictWriter(dataset_csv, fieldnames=self.keys)
        #     if dataset_csv == None:
        #         dataset.writeheader()
        #     data_list = []
        #     for hasil in self.hasil_ekstraksi:
        #         data = {}
        #         for i in range(len(hasil)):
        #             data[self.keys[i]] = hasil[i]
        #         data_list.append(data)
        #     dataset.writerows(data_list)
        #     print(dataset)

        if self.dataset != []:
            self.lbl_memakai.setPixmap(QtGui.QPixmap(
                "E:/Project/Deteksi_Masker_Project/assets/icons/checked.png"))

    def kls_tidak_memakai(self):
        self.load()
        kelas = ['Tidak Memakai']
        for nama, ekstrak in zip(self.nama_file, self.hasil_ekstraksi):
            nama = [nama]
            hasil = nama + ekstrak + kelas
            self.dataset.append(hasil)

        if self.dataset != []:
            self.lbl_tdk_memakai.setPixmap(QtGui.QPixmap(
                "E:/Project/Deteksi_Masker_Project/assets/icons/checked.png"))

    def final(self):
        if self.dataset == []:
            self.lbl_peringatan.setText(
                "Silahkan masukkan citra untuk kedua kelas data terlebih dahulu!!!")

        else:
            df = pd.DataFrame(self.dataset, columns=self.keys)
            # cek untuk ketersediaan data kedua kelas
            kelas = np.array(df['Class'])

            if len(np.unique(kelas)) == 2:
                df.to_csv(
                    'E:/Project/Deteksi_Masker_Project/dataset/dataset.csv', index=False)
                self.close()
            else:
                self.lbl_peringatan.setText(
                    "Silahkan masukkan citra untuk kedua kelas data terlebih dahulu!!!")

    def retranslateUi(self, form_kelas):
        _translate = QtCore.QCoreApplication.translate
        form_kelas.setWindowTitle(_translate(
            "form_kelas", "Kelas Data Ekstraksi"))
        self.label.setText(_translate(
            "form_kelas", "Pilih Kelas Data Hasil Ekstraksi GCLM :"))
        self.btn_memakai.setText(_translate("form_kelas", "MEMAKAI MASKER"))
        self.btn_tidak_memakai.setText(_translate(
            "form_kelas", "TIDAK MEMAKAI MASKER"))
        self.lbl_memakai.setText(_translate(
            "form_kelas", ""))
        self.lbl_tdk_memakai.setText(_translate(
            "form_kelas", ""))
        self.lbl_peringatan.setText(_translate(
            "form_kelas", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_form_kelas()
    ui.show()
    sys.exit(app.exec_())
