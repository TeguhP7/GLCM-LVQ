from PyQt5 import QtCore, QtGui, QtWidgets
import training_page
import deteksi_masker
import about


class Ui_Landing_Page(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Landing_Page, self).__init__()
        self.setObjectName("Landing_Page")
        self.resize(931, 608)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "E:/Project/Deteksi_Masker_Project/assets/icons/mask.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setToolTip("")
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setAutoFillBackground(False)
        self.setStyleSheet(
            "QMainWindow#Landing_Page{background-color:rgb(255, 255, 255)}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gambar = QtWidgets.QLabel(self.centralwidget)
        self.gambar.setGeometry(QtCore.QRect(0, 0, 531, 620))
        self.gambar.setToolTipDuration(0)
        self.gambar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gambar.setAutoFillBackground(False)
        self.gambar.setStyleSheet(
            "QLabel#gambar{background-image:url(E:/Project/Deteksi_Masker_Project/assets/wallpapers/landing1.jpg)}")
        self.gambar.setLineWidth(0)
        self.gambar.setText("")
        self.gambar.setAlignment(QtCore.Qt.AlignCenter)
        self.gambar.setWordWrap(True)
        self.gambar.setIndent(0)
        self.gambar.setObjectName("gambar")
        self.btn_training = QtWidgets.QPushButton(self.centralwidget)
        self.btn_training.setGeometry(QtCore.QRect(590, 270, 281, 41))
        self.btn_training.setStyleSheet("color:white; background-color:rgb(85, 85, 255); border-radius:20px;\n"
                                        "font: 87 10pt \"Segoe UI Black\";")
        self.btn_training.setObjectName("btn_training")
        self.btn_training.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_training.clicked.connect(
            self.training_page)  # connect ke halaman training
        self.btn_training.clicked.connect(
            self.close)

        self.btn_testing = QtWidgets.QPushButton(self.centralwidget)
        self.btn_testing.setGeometry(QtCore.QRect(590, 410, 281, 41))
        self.btn_testing.setStyleSheet("color:white; background-color:rgb(85, 85, 255); border-radius:20px;\n"
                                       "font: 87 10pt \"Segoe UI Black\";")
        self.btn_testing.setObjectName("btn_testing")
        self.btn_testing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_testing.clicked.connect(
            self.testing_page)  # connect ke halaman testing
        self.btn_testing.clicked.connect(
            self.close)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 315, 261, 51))
        self.label_3.setStyleSheet("color:rgb(130, 130, 130)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 450, 261, 51))
        self.label_4.setStyleSheet("color:rgb(130, 130, 130)")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(625, 170, 211, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(625, 80, 211, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 540, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(555, 550, 351, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(603, 100, 254, 71))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Richela Kids")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(0, 170, 255)")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btn_about = QtWidgets.QPushButton(self.centralwidget)
        self.btn_about.setGeometry(QtCore.QRect(840, 140, 50, 50))
        self.btn_about.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_about.setAccessibleName("")
        self.btn_about.setStyleSheet("background-color:white")
        self.btn_about.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "E:/Project/Deteksi_Masker_Project/assets/icons/paper-plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_about.setIcon(icon1)
        self.btn_about.setIconSize(QtCore.QSize(40, 40))
        self.btn_about.setShortcut("")
        self.btn_about.setFlat(True)
        self.btn_about.setObjectName("btn_about")
        self.btn_about.clicked.connect(self.about_page)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(856, 183, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold Condensed")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(136, 136, 136)")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_2.raise_()
        self.gambar.raise_()
        self.label.raise_()
        self.btn_training.raise_()
        self.btn_testing.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_5.raise_()
        self.line_3.raise_()
        self.btn_about.raise_()
        self.label_6.raise_()
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def training_page(self):
        self.gui_training = training_page.Ui_Training_Page()
        self.gui_training.show()

    def testing_page(self):
        self.gui_testing = deteksi_masker.Ui_MainWindow()
        self.gui_testing.show()

    def about_page(self):
        self.about = QtWidgets.QDialog()
        self.gui_about = about.Ui_about()
        self.gui_about.setupUi(self.about)
        self.about.show()

    def retranslateUi(self, Landing_Page):
        _translate = QtCore.QCoreApplication.translate
        Landing_Page.setWindowTitle(_translate(
            "Landing_Page", "Deteksi Masker App"))
        self.btn_training.setText(_translate("Landing_Page", "TRAINING"))
        self.btn_testing.setText(_translate("Landing_Page", "TESTING"))
        self.label_3.setText(_translate(
            "Landing_Page", "Poses training merupakan proses pelatihan data yang akan menghasilkan bobot optimal untuk digunakan dalam proses  testing"))
        self.label_4.setText(_translate(
            "Landing_Page", "Poses testing merupakan proses pengujian data dengan nilai bobot optimal dari proses training"))
        self.label_5.setText(_translate(
            "Landing_Page", "Silahkan pilih TESTING untuk masuk ke halaman Deteksi Masker"))
        self.label.setText(_translate("Landing_Page", "SELAMAT DATANG!"))
        self.label_2.setText(_translate(
            "Landing_Page", "Deteksi Masker App v.01"))
        self.label_6.setText(_translate("Landing_Page", "click me!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Landing_Page()
    ui.show()
    sys.exit(app.exec_())
