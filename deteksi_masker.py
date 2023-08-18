from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import GUI_Dataset
import sys
from os import path
import cv2 as cv
import glcm_fitur
import lvq
import training_page


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(931, 608)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "E:/Project/Deteksi_Masker_Project/assets/icons/mask.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet(
            "QMainWindow{background-image:url(E:/Project/Deteksi_Masker_Project/assets/wallpapers/bg2.jpg)}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gambarOri = QtWidgets.QLabel(self.centralwidget)
        self.gambarOri.setGeometry(QtCore.QRect(60, 80, 231, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gambarOri.setFont(font)
        self.gambarOri.setStyleSheet(
            "background-color:rgb(255, 255, 255); border-radius:20px")
        self.gambarOri.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gambarOri.setFrameShadow(QtWidgets.QFrame.Plain)
        self.gambarOri.setLineWidth(1)
        self.gambarOri.setScaledContents(True)
        self.gambarOri.setAlignment(QtCore.Qt.AlignCenter)
        self.gambarOri.setObjectName("gambarOri")
        self.text_judul = QtWidgets.QLabel(self.centralwidget)
        self.text_judul.setGeometry(QtCore.QRect(70, 0, 791, 61))
        self.text_judul.setStyleSheet("color:white;\n"
                                      "font: 27pt \"Wild Nature\";")
        self.text_judul.setWordWrap(True)
        self.text_judul.setObjectName("text_judul")
        self.btn_deteksi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_deteksi.setGeometry(QtCore.QRect(340, 210, 111, 41))
        self.btn_deteksi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_deteksi.setStyleSheet("color:white;background-color:rgb(85, 85, 255); border-radius:20px;\n"
                                       "font: 87 10pt \"Segoe UI Black\";")
        self.btn_deteksi.setObjectName("btn_deteksi")
        self.btn_deteksi.clicked.connect(
            self.gambar_grayscale)  # connect ekstraksi fitur

        self.gambarGray = QtWidgets.QLabel(self.centralwidget)
        self.gambarGray.setGeometry(QtCore.QRect(60, 330, 226, 226))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gambarGray.setFont(font)
        self.gambarGray.setStyleSheet(
            "background-color:rgb(255, 255, 255); border-radius:20px; border-width: 110px; border-color: rgb(0, 0, 147);")
        self.gambarGray.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gambarGray.setFrameShadow(QtWidgets.QFrame.Plain)
        self.gambarGray.setLineWidth(1)
        self.gambarGray.setAlignment(QtCore.Qt.AlignCenter)
        self.gambarGray.setObjectName("gambarGray")
        self.label_hasil = QtWidgets.QLabel(self.centralwidget)
        self.label_hasil.setGeometry(QtCore.QRect(585, 135, 91, 31))
        self.label_hasil.setStyleSheet("font: 75 8pt \"News706 BT\";")
        self.label_hasil.setObjectName("label_hasil")
        self.hasil = QtWidgets.QLabel(self.centralwidget)
        self.hasil.setGeometry(QtCore.QRect(580, 160, 251, 91))
        self.hasil.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                 "font: 30pt \"Phoresta\";\n"
                                 "border-radius:15px;")
        self.hasil.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hasil.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hasil.setLineWidth(1)
        self.hasil.setText("")
        self.hasil.setAlignment(QtCore.Qt.AlignCenter)
        self.hasil.setObjectName("hasil")
        self.btn_pilihGambar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pilihGambar.setGeometry(QtCore.QRect(340, 150, 111, 41))
        self.btn_pilihGambar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_pilihGambar.setStyleSheet("color:white;background-color:rgb(85, 85, 255); border-radius:20px;\n"
                                           "font: 87 10pt \"Segoe UI Black\";")
        self.btn_pilihGambar.setObjectName("btn_pilihGambar")
        self.btn_pilihGambar.clicked.connect(
            self.buka_gambar)  # Memilih gambar/foto dari file

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(340, 350, 541, 206))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label_hasil_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_hasil_2.setGeometry(QtCore.QRect(340, 320, 51, 31))
        self.label_hasil_2.setStyleSheet("font: 75 8pt \"News706 BT\";")
        self.label_hasil_2.setObjectName("label_hasil_2")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 21))
        self.menubar.setObjectName("menubar")
        self.menuBerkas = QtWidgets.QMenu(self.menubar)
        self.menuBerkas.setObjectName("menuBerkas")
        self.menuDataset = QtWidgets.QMenu(self.menubar)
        self.menuDataset.setObjectName("menuDataset")
        # self.menuBantuan = QtWidgets.QMenu(self.menubar)
        # self.menuBantuan.setObjectName("menuBantuan")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionBuka = QtWidgets.QAction(self)
        self.actionBuka.setObjectName("actionBuka")
        self.actionBuka.triggered.connect(
            self.buka_gambar)  # connect buka gambar

        self.actionKeluar = QtWidgets.QAction(self)
        self.actionKeluar.setObjectName("actionKeluar")
        self.actionKeluar.triggered.connect(
            self.close)  # connect keluar app

        self.actionLihat = QtWidgets.QAction(self)
        self.actionLihat.setObjectName("actionLihat")
        self.actionLihat.triggered.connect(
            self.ui_dataset)  # connect dataset
        # self.actionLihat.triggered.connect(self.close)

        self.actionTraining = QtWidgets.QAction(self)
        self.actionTraining.setObjectName("actionTraining")
        self.actionTraining.triggered.connect(
            self.gui_training)  # connect dataset

        # self.actionCara_Penggunaan = QtWidgets.QAction(self)
        # self.actionCara_Penggunaan.setObjectName("actionCara_Penggunaan")
        # self.actionInfo = QtWidgets.QAction(self)
        # self.actionInfo.setObjectName("actionInfo")
        self.menuBerkas.addAction(self.actionBuka)
        self.menuBerkas.addSeparator()
        self.menuBerkas.addAction(self.actionKeluar)
        self.menuDataset.addAction(self.actionLihat)
        self.menuDataset.addAction(self.actionTraining)
        # self.menuBantuan.addAction(self.actionCara_Penggunaan)
        # self.menuBantuan.addAction(self.actionInfo)
        self.menubar.addAction(self.menuBerkas.menuAction())
        self.menubar.addAction(self.menuDataset.menuAction())
        # self.menubar.addAction(self.menuBantuan.menuAction())
        ######################################
        # Variable Bebas
        ######################################

        self.raw_data = None
        self.image = None
        self.gray = None

        ######################################

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def buka_gambar(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Select Image File',
                                                          filter="All (*);;JPEG (*.jpg);;PNG(*.png)")
        if file_name[0]:
            self.image = file_name[0]
            self.f_type = path.splitext(file_name[0])
            (self.directory, self.filename) = path.split(self.image)
            self.raw_data = np.array(cv.imread(
                self.image))
            self.image = self.ukuran(self.raw_data)
        elif self. raw_data is None:
            self.buka_gambar()

    def ukuran(self, gambar):
        self.image = gambar
        h, w = self.image.shape[:2]
        max_height = 300
        max_width = 300
        if max_height <= h or max_width <= w:
            # get scaling factor
            scaling_factor = max_height / float(h)
            if max_width/float(w) < scaling_factor:
                scaling_factor = max_width / float(w)
            # resize image
            self.image = cv.resize(self.image, None, fx=scaling_factor,
                                   fy=scaling_factor, interpolation=cv.INTER_AREA)
        elif max_height > h or max_width > w:
            scaling_factor = max_height / float(h)
            # resize image
            self.image = cv.resize(self.image, None, fx=scaling_factor,
                                   fy=scaling_factor, interpolation=cv.INTER_AREA)

        view = self.displayImage(self.image)
        self.gambarOri.setPixmap(QtGui.QPixmap.fromImage(view))
        self.gambarOri.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)

        return self.image

    def displayImage(self, gambar):
        # self.image = gambar
        qformat = QtGui.QImage.Format.Format_Indexed8
        if len(gambar.shape) == 3:
            if (gambar.shape[2]) == 4:
                qformat = QtGui.QImage.Format.Format_RGBA8888
            else:
                qformat = QtGui.QImage.Format.Format_RGB888

        img = QtGui.QImage(
            gambar.copy(), gambar.copy().shape[1], gambar.copy().shape[0], gambar.copy().strides[0], qformat)

        img = img.rgbSwapped()
        return img

    def ui_dataset(self):
        self.lihat_dataset_ui = QtWidgets.QDialog()
        self.gui_data = GUI_Dataset.Ui_form_dataset()
        self.gui_data.setupUi(self.lihat_dataset_ui)
        self.lihat_dataset_ui.show()

    def gui_training(self):
        self.training = training_page.Ui_Training_Page()
        self.training.show()

    def gambar_grayscale(self):
        img_gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)

        # Gambar Grayscale
        view = self.displayImage(img_gray)
        self.gambarGray.setPixmap(QtGui.QPixmap.fromImage(view))
        self.gambarGray.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.ekstraksi_fitur()

    def ekstraksi_fitur(self):
        modul = glcm_fitur.Fungsi
        preprocessing_img = modul.preprocessing(self.raw_data)
        self.data = modul.ekstraksi(preprocessing_img)
        fitur = np.array(self.data)
        # print(fitur)
        x = 0
        y = 0
        for dataa in fitur:
            self.tableWidget.setItem(
                x, y, QtWidgets.QTableWidgetItem(str(dataa)))
            y += 1

        self.metode_lvq()

    def metode_lvq(self):
        x_test = np.array(self.data)

        df_bobot = pd.read_csv(
            'E:/Project/Deteksi_Masker_Project/dataset/bobot_lvq_dataset_hasil2(100-0.001).csv')
        bobot = df_bobot.iloc[:, :-1]
        label_bobot = df_bobot['Class']

        bobot = np.array(bobot)
        label_bobot = np.array(label_bobot)
        bobot_dan_label = (bobot, label_bobot)
        # print(bobot_dan_label)

        # Testing
        y_pred = lvq.LVQ.test(self=lvq.LVQ, test_data=x_test,
                              weight_class=bobot_dan_label)
        # print('Label Pred: ', y_pred)
        # print('Label True: ', y_test)
        # print('Accuracy:', accuracy_score(y_train, y_pred))
        # print('Class', y_pred)
        hasil = y_pred
        self.hasil.setText(hasil)

    # def close_application(self):
    #     choice = QtWidgets.QMessageBox.question(self, 'Keluar', 'Apa kamu yakin keluar aplikasi?',
    #                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
    #     if choice == QtWidgets.QMessageBox.Yes:
    #         sys.exit()
    #     else:
    #         pass

    # Fungsi Exit bawaan librari untuk MainWindow (Otomatis dipanggil)
    def closeEvent(self, event):
        pilih = QtWidgets.QMessageBox.question(self, 'Keluar', 'Apa kamu yakin keluar aplikasi?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if pilih == QtWidgets.QMessageBox.Yes:
            # print("App Closed!")
            event.accept()
        else:
            event.ignore()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Deteksi Masker App"))
        self.gambarOri.setText(_translate("MainWindow", "ORIGINAL"))
        self.text_judul.setText(_translate(
            "MainWindow", "SELAMAT DATANG DI APLIKASI DETEKSI PENGGUNAAN MASKER"))
        self.btn_deteksi.setText(_translate("MainWindow", "DETEKSI"))
        self.gambarGray.setText(_translate("MainWindow", "GRAYSCALE"))
        self.label_hasil.setText(_translate("MainWindow", u"Hasil Deteksi :"))
        self.btn_pilihGambar.setText(_translate("MainWindow", "Pilih Gambar"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Correlation"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Homogeneity"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Dissimilarity"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Contrast"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Energy"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "ASM"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "0\'"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "45\'"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "90\'"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "135\'"))
        self.label_hasil_2.setText(_translate("MainWindow", "Fitur :"))
        self.menuBerkas.setTitle(_translate("MainWindow", "File"))
        self.menuDataset.setTitle(_translate("MainWindow", "Dataset"))
        self.actionBuka.setText(_translate("MainWindow", "Buka"))
        self.actionKeluar.setText(_translate("MainWindow", "Keluar"))
        self.actionLihat.setText(_translate("MainWindow", "Lihat"))
        self.actionTraining.setText(_translate(
            "MainWindow", "Pelatihan Data (Training)"))
        # self.menuBantuan.setTitle(_translate("MainWindow", "Bantuan"))
        # self.actionCara_Penggunaan.setText(
        #     _translate("MainWindow", "Cara Penggunaan"))
        # self.actionInfo.setText(_translate("MainWindow", "Info"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = Ui_MainWindow()
    # windows.setWindowIcon(QtGui.QIcon('Skripsi/icon/theater.png'))
    # windows.setStyleSheet(
    #     "QMainWindow{background-image:url(E:/Project/Skripsi/wallpaper/bg2.jpg)}")
    windows.show()
    sys.exit(app.exec_())
