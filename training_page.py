from PyQt5 import QtCore, QtGui, QtWidgets
import form_kelas
import form_parameter_LVQ
import deteksi_masker
import pandas as pd
import numpy as np


class Ui_Training_Page(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Training_Page, self).__init__()
        self.setObjectName("Training_Page")
        self.resize(931, 625)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "E:/Project/Deteksi_Masker_Project/assets/icons/mask.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        # E:/Project/Deteksi_Masker_Project/assets/wallpapers/landing.jpg
        self.setStyleSheet(
            "QMainWindow#Training_Page{background-image:url(E:/Project/Deteksi_Masker_Project/assets/wallpapers/bg2.jpg)}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tbl_ekstraksiGLCM = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_ekstraksiGLCM.setGeometry(QtCore.QRect(20, 100, 891, 281))
        self.tbl_ekstraksiGLCM.setStyleSheet("")
        self.tbl_ekstraksiGLCM.setRowCount(30)
        self.tbl_ekstraksiGLCM.setColumnCount(26)
        self.tbl_ekstraksiGLCM.setObjectName("tbl_ekstraksiGLCM")
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ekstraksiGLCM.setHorizontalHeaderItem(25, item)
        self.btn_ekstraksi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ekstraksi.setGeometry(QtCore.QRect(40, 23, 151, 41))
        self.btn_ekstraksi.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ekstraksi.setStyleSheet("color:white; background-color:blue; border-radius:20px;\n"
                                         "font: 87 10pt \"Segoe UI Black\";")
        self.btn_ekstraksi.setObjectName("btn_ekstraksi")
        self.btn_ekstraksi.clicked.connect(self.ekstraksi)

        # self.btn_hapus_dataset = QtWidgets.QPushButton(self.centralwidget)
        # self.btn_hapus_dataset.setGeometry(QtCore.QRect(220, 23, 151, 41))
        # self.btn_hapus_dataset.setCursor(
        #     QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.btn_hapus_dataset.setStyleSheet("background-color:rgb(255, 0, 0); color:white; border-radius:20px;\n"
        #                                      "font: 87 10pt \"Segoe UI Black\";")
        # self.btn_hapus_dataset.setObjectName("btn_hapus_dataset")
        # self.btn_hapus_dataset.clicked.connect(self.deteksi_page)

        self.btn_LVQ = QtWidgets.QPushButton(self.centralwidget)
        self.btn_LVQ.setGeometry(QtCore.QRect(40, 405, 151, 41))
        self.btn_LVQ.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_LVQ.setStyleSheet("background-color:green; color:white; border-radius:20px;\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.btn_LVQ.setObjectName("btn_LVQ")
        self.btn_LVQ.clicked.connect(self.klasifikasi_LVQ)

        self.tbl_bobotLVQ = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_bobotLVQ.setGeometry(QtCore.QRect(20, 480, 891, 105))
        self.tbl_bobotLVQ.setStyleSheet("")
        self.tbl_bobotLVQ.setRowCount(30)
        self.tbl_bobotLVQ.setColumnCount(25)
        self.tbl_bobotLVQ.setObjectName("tbl_bobotLVQ")
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_bobotLVQ.setHorizontalHeaderItem(24, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 460, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255,255,255)")
        self.label.setObjectName("label")
        self.label.setStyleSheet('color:black')
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255,255,255)")
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet('color:black')
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 20, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Humnst777 BlkCn BT")
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: white;color:black")
        self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setLineWidth(1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 400, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Humnst777 BlkCn BT")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:black;background-color:white")
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setLineWidth(1)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menuBar.setObjectName("menuBar")
        self.setMenuBar(self.menuBar)
        self.menuPage = QtWidgets.QMenu(self.menuBar)
        self.menuPage.setObjectName("menuPage")
        self.setMenuBar(self.menuBar)
        self.actionDeteksi_Masker_testing = QtWidgets.QAction(self)
        self.actionDeteksi_Masker_testing.setObjectName(
            "actionDeteksi_Masker_testing")
        self.actionDeteksi_Masker_testing.triggered.connect(self.deteksi_page)

        self.actionKeluar = QtWidgets.QAction(self)
        self.actionKeluar.setObjectName("actionKeluar")
        self.actionKeluar.triggered.connect(self.close)

        self.menuPage.addAction(self.actionDeteksi_Masker_testing)
        self.menuPage.addSeparator()
        self.menuPage.addAction(self.actionKeluar)
        self.menuBar.addAction(self.menuPage.menuAction())

        # Menampilkan dataset

        dataset1 = pd.read_csv(
            'E:/Project/Deteksi_Masker_Project/dataset/New_Dataset_Masker.csv')
        # dataset2 = np.array(pd.read_csv(
        #     'E:/Project/Deteksi_Masker_Project/dataset/dataset.csv'))
        data1 = np.array(dataset1)
        self.tbl_ekstraksiGLCM.setRowCount(0)
        for row_number, row_data in enumerate(data1):
            self.tbl_ekstraksiGLCM.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tbl_ekstraksiGLCM.setItem(
                    row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))

        df_bobot = pd.read_csv(
            'E:/Project/Deteksi_Masker_Project/dataset/bobot_lvq.csv')
        bobot = np.array(df_bobot)
        self.tbl_bobotLVQ.setRowCount(0)
        for row_number, row_data in enumerate(bobot):
            self.tbl_bobotLVQ.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tbl_bobotLVQ.setItem(
                    row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def ekstraksi(self):
        self.form_kelas = form_kelas.Ui_form_kelas()
        self.form_kelas.show()

    def deteksi_page(self):
        self.testing = deteksi_masker.Ui_MainWindow()
        self.testing.show()

    def klasifikasi_LVQ(self):
        self.form_LVQ = form_parameter_LVQ.Ui_parameter_LVQ()
        self.form_LVQ.show()

    def closeEvent(self, event):
        pilih = QtWidgets.QMessageBox.question(self, 'Keluar', 'Apa kamu yakin keluar aplikasi?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if pilih == QtWidgets.QMessageBox.Yes:
            # print("App Closed!")
            event.accept()
        else:
            event.ignore()

    def retranslateUi(self, Training_Page):
        _translate = QtCore.QCoreApplication.translate
        Training_Page.setWindowTitle(_translate(
            "Training_Page", "Deteksi Masker App - Data Training"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(0)
        item.setText(_translate("Training_Page", "File"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(1)
        item.setText(_translate("Training_Page", "Correlation 0\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(2)
        item.setText(_translate("Training_Page", "Correlation 45\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(3)
        item.setText(_translate("Training_Page", "Correlation 90\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(4)
        item.setText(_translate("Training_Page", "Correlation 135\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(5)
        item.setText(_translate("Training_Page", "Homogeneity 0\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(6)
        item.setText(_translate("Training_Page", "Homogeneity  45"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(7)
        item.setText(_translate("Training_Page", "Homogeneity 90\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(8)
        item.setText(_translate("Training_Page", "Homogeneity 135\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(9)
        item.setText(_translate("Training_Page", "Dissimilarity 0\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(10)
        item.setText(_translate("Training_Page", "Dissimilarity  45"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(11)
        item.setText(_translate("Training_Page", "Dissimilarity 90\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(12)
        item.setText(_translate("Training_Page", "Dissimilarity 135\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(13)
        item.setText(_translate("Training_Page", "Contrast 0\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(14)
        item.setText(_translate("Training_Page", "Contrast  45"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(15)
        item.setText(_translate("Training_Page", "Contrast 90\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(16)
        item.setText(_translate("Training_Page", "Contrast 135\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(17)
        item.setText(_translate("Training_Page", "Energy 0\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(18)
        item.setText(_translate("Training_Page", "Energy  45"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(19)
        item.setText(_translate("Training_Page", "Energy 90\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(20)
        item.setText(_translate("Training_Page", "Energy 135\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(21)
        item.setText(_translate("Training_Page", "ASM 0\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(22)
        item.setText(_translate("Training_Page", "ASM 45"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(23)
        item.setText(_translate("Training_Page", "ASM 90\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(24)
        item.setText(_translate("Training_Page", "ASM 135\'"))
        item = self.tbl_ekstraksiGLCM.horizontalHeaderItem(25)
        item.setText(_translate("Training_Page", "Class"))
        self.btn_ekstraksi.setText(_translate(
            "Training_Page", "EKSTRAKSI GAMBAR"))
        # self.btn_hapus_dataset.setText(
        #     _translate("Training_Page", "HAPUS DATASET"))
        self.btn_LVQ.setText(_translate("Training_Page", "TRAINING LVQ"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(0)
        item.setText(_translate("Training_Page", "Correlation 0\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(1)
        item.setText(_translate("Training_Page", "Correlation 45\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(2)
        item.setText(_translate("Training_Page", "Correlation 90\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(3)
        item.setText(_translate("Training_Page", "Correlation 135\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(4)
        item.setText(_translate("Training_Page", "Homogeneity 0\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(5)
        item.setText(_translate("Training_Page", "Homogeneity  45"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(6)
        item.setText(_translate("Training_Page", "Homogeneity 90\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(7)
        item.setText(_translate("Training_Page", "Homogeneity 135\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(8)
        item.setText(_translate("Training_Page", "Dissimilarity 0\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(9)
        item.setText(_translate("Training_Page", "Dissimilarity  45"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(10)
        item.setText(_translate("Training_Page", "Dissimilarity 90\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(11)
        item.setText(_translate("Training_Page", "Dissimilarity 135\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(12)
        item.setText(_translate("Training_Page", "Contrast 0\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(13)
        item.setText(_translate("Training_Page", "Contrast  45"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(14)
        item.setText(_translate("Training_Page", "Contrast 90\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(15)
        item.setText(_translate("Training_Page", "Contrast 135\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(16)
        item.setText(_translate("Training_Page", "Energy 0\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(17)
        item.setText(_translate("Training_Page", "Energy  45"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(18)
        item.setText(_translate("Training_Page", "Energy 90\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(19)
        item.setText(_translate("Training_Page", "Energy 135\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(20)
        item.setText(_translate("Training_Page", "ASM 0\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(21)
        item.setText(_translate("Training_Page", "ASM 45"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(22)
        item.setText(_translate("Training_Page", "ASM 90\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(23)
        item.setText(_translate("Training_Page", "ASM 135\'"))
        item = self.tbl_bobotLVQ.horizontalHeaderItem(24)
        item.setText(_translate("Training_Page", "Class"))
        self.label.setText(_translate("Training_Page", "Bobot Optimal :"))
        self.label_2.setText(_translate("Training_Page", "Ekstraksi GLCM :"))
        self.label_3.setText(_translate(
            "Training_Page", "MELAKUKAN EKSTRAKSI GLCM BARU, AKAN MENGGANTI DATASET EKSTRAKSI GLCM SEBELUMNYA"))
        self.label_4.setText(_translate(
            "Training_Page", "JANGAN LUPA MELAKUKAN TRAINING LVQ AGAR MEMPEROLEH BOBOT BARU, SETELAH MEMASUKKAN DATA EKSTRAKSI GLCM BARU"))
        self.menuPage.setTitle(_translate("Training_Page", "Page"))
        self.actionDeteksi_Masker_testing.setText(
            _translate("Training_Page", "Deteksi Masker (Testing)"))
        self.actionKeluar.setText(_translate("Training_Page", "Keluar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Training_Page()
    ui.show()
    sys.exit(app.exec_())