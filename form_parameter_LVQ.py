from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import lvq


class Ui_parameter_LVQ(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_parameter_LVQ, self).__init__()
        self.setObjectName("parameter_LVQ")
        self.resize(282, 227)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "E:/Project/Deteksi_Masker_Project/assets/icons/mask.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet(
            "QDialog#parameter_LVQ{background-image:url(E:/Project/Deteksi_Masker_Project/assets/wallpapers/bg3.jpg)}")
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(65, 180, 156, 23))
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.onOk)
        self.buttonBox.rejected.connect(self.reject)

        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 20, 241, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_epoch = QtWidgets.QLabel(self.layoutWidget)
        self.label_epoch.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_epoch.setObjectName("label_epoch")
        self.gridLayout.addWidget(self.label_epoch, 0, 0, 1, 1)
        self.input_epoch = QtWidgets.QSpinBox(
            self.layoutWidget, value=10, maximum=100000, minimum=10, singleStep=10)  # input epoch
        self.input_epoch.setObjectName("input_epoch")
        self.gridLayout.addWidget(self.input_epoch, 0, 1, 1, 1)
        self.label_alpha = QtWidgets.QLabel(self.layoutWidget)
        self.label_alpha.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_alpha.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_alpha.setObjectName("label_alpha")
        self.gridLayout.addWidget(self.label_alpha, 1, 0, 1, 1)
        self.input_alpha = QtWidgets.QDoubleSpinBox(
            self.layoutWidget, value=0.0001, maximum=1, minimum=0.0001, singleStep=0.0001)  # input alpha
        self.input_alpha.setDecimals(4)
        self.input_alpha.setObjectName("input_alpha")
        self.gridLayout.addWidget(self.input_alpha, 1, 1, 1, 1)
        self.label_min_alpha = QtWidgets.QLabel(self.layoutWidget)
        self.label_min_alpha.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_min_alpha.setObjectName("label_min_alpha")
        self.gridLayout.addWidget(self.label_min_alpha, 2, 0, 1, 1)
        self.input_min_alpha = QtWidgets.QDoubleSpinBox(
            self.layoutWidget, value=0.00001, maximum=1, minimum=0.00001, singleStep=0.00001)  # input min. alpha
        self.input_min_alpha.setDecimals(5)
        self.input_min_alpha.setObjectName("input_min_alpha")
        self.gridLayout.addWidget(self.input_min_alpha, 2, 1, 1, 1)
        self.label_dec_alpha = QtWidgets.QLabel(self.layoutWidget)
        self.label_dec_alpha.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_dec_alpha.setObjectName("label_dec_alpha")
        self.gridLayout.addWidget(self.label_dec_alpha, 3, 0, 1, 1)
        self.input_dec_alpha = QtWidgets.QDoubleSpinBox(
            self.layoutWidget, value=0.1, maximum=1, minimum=0.1, singleStep=0.1)  # input decrease alpha
        self.input_dec_alpha.setDecimals(1)
        self.input_dec_alpha.setObjectName("input_dec_alpha")
        self.gridLayout.addWidget(self.input_dec_alpha, 3, 1, 1, 1)

        fitur_glcm = ['correlation', 'homogeneity',
                      'dissimilarity', 'contrast', 'energy', 'ASM']
        arah_sudut = ['0', '45', '90', '135']
        self.keys = []
        for fitur in fitur_glcm:
            for sudut in arah_sudut:
                key = fitur+'_'+sudut
                self.keys.append(key)
        self.keys.append('Class')

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def onOk(self):
        self.epoch = int(self.input_epoch.text())
        self.alpha = float(self.input_alpha.text())
        self.min_alpha = float(self.input_min_alpha.text())
        self.dec_alpha = float(self.input_dec_alpha.text())

        self.training_lvq()

    def training_lvq(self):
        dataset = pd.read_csv(
            "E:/Project/Deteksi_Masker_Project/dataset/dataset_hasil/dataset_hasil2.csv")
        data = dataset.iloc[:, 1:-1]
        label = dataset['Class']
        x_train = np.array(data)
        y_train = np.array(label)

        n_input = x_train.shape[1]
        n_output = len(np.unique(y_train))

        # LVQ
        # Training
        metode_lvq = lvq.LVQ(sizeInput=n_input, sizeOutput=n_output,
                             max_epoch=self.epoch, alpha=self.alpha, minalpha=self.min_alpha, decalpha=self.dec_alpha)
        self.bobot_dan_label = metode_lvq.train(x_train, y_train)
        bobot, label = self.bobot_dan_label
        bobot = bobot.tolist()
        label = label.tolist()
        hasil_lvq = []
        for i in range(len(label)):
            hasil = bobot[i] + [label[i]]
            hasil_lvq.append(hasil)
        df = pd.DataFrame(hasil_lvq, columns=self.keys)
        df.to_csv(
            'E:/Project/Deteksi_Masker_Project/dataset/bobot_lvq_dataset_hasil2('+str(self.epoch)+'-'+str(self.alpha)+').csv', index=False)
        self.close()

    def retranslateUi(self, parameter_LVQ):
        _translate = QtCore.QCoreApplication.translate
        parameter_LVQ.setWindowTitle(
            _translate("parameter_LVQ", "Parameter LVQ"))
        self.label_epoch.setText(_translate("parameter_LVQ", "epoch  ="))
        self.label_alpha.setText(_translate(
            "parameter_LVQ", "learning rate (alpha)="))
        self.label_min_alpha.setText(_translate(
            "parameter_LVQ", "minimum alpha ="))
        self.label_dec_alpha.setText(_translate(
            "parameter_LVQ", "decrease alpha ="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_parameter_LVQ()
    ui.show()
    sys.exit(app.exec_())
