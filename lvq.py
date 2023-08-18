import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


class LVQ(object):

    def __init__(self, sizeInput, sizeOutput, max_epoch, alpha, minalpha, decalpha=0.1):
        """
        Inisialisasi class (constructor)
        :param sizeInput (int): Banyaknya input neuron sesuai dengan banyaknya parameter (fitur pada data latih)
        :param sizeOutput (int): Banyaknya output neuron sesuai dengan banyaknya label (kelas pada data latih)
        :param max_epoch (int): Maksimal epoch yang diizinkan
        :param alpha (float): learning rate
        :param minalpha (float): minimum learning rate

        """

        self.sizeInput = sizeInput
        self.sizeOutput = sizeOutput
        self.max_epoch = max_epoch
        self.alpha = alpha
        self.minalpha = minalpha
        self.decalpha = decalpha
        self.weight = np.zeros((sizeOutput, sizeInput))

    def get(self):
        """
        Mendapatkan bobot jaringan LVQ setelah proses training

        :return: weight (nilai bobot)
        """

        return self.weight, self.weight_label

    def train(self, train_data, train_target):
        """
        Proses pelatihan jaringan LVQ
        :param train_data (numpy array atau pandas dataframe): Matriks yang berisi data latih
        :param train_target (numpy array atau pandas series): Array yang berisi label dari data latih
        :return: bobot dan label dari bobot
        """
        # print('train target:', train_target)
        self.weight_label, label_index = np.unique(train_target, True)
        # print('weight_label'+str(weight_label))
        # print('label_index'+str(label_index))

        # Inisialisasi bobot
        self.weight = train_data[label_index].astype(np.float64)
        # print('label_index'+str(self.weight))
        # print('train_data', train_data)

        # Hapus data yang digunakan untuk inisialisasi bobot
        train_data = np.delete(train_data, label_index, axis=0)
        # print('train_data2', train_data)
        train_target = np.delete(train_target, label_index, axis=0)
        # print('train_target', train_target)

        epoch = 0
        # or self.alpha >= self.minalpha
        while epoch <= self.max_epoch :
            epoch += 1
            # print('\nEpoch', epoch)
            for data, target in zip(train_data, train_target):
                # iterasi += 1
                # print('Iterasi', iterasi)
                distance = np.sqrt(np.sum((data - self.weight) ** 2, axis=1))
                # print('jarak =', distance)
                idx_min = np.argmin(distance)
                # print(idx_min)
                if target == self.weight_label[idx_min]:
                    self.weight[idx_min] = self.weight[idx_min] + \
                        self.alpha * (data - self.weight[idx_min])
                else:
                    self.weight[idx_min] = self.weight[idx_min] - \
                        self.alpha * (data - self.weight[idx_min])

            self.alpha = self.alpha - (self.alpha*self.decalpha)
            # self.alpha = self.alpha * (1 - epoch / self.max_epoch)

        weight_class = (self.weight, self.weight_label)
        return weight_class

    def test(self, test_data, weight_class):
        """
        Proses pengujian jaringan LVQ
        :param test_data (numpy array atau pandas dataframe): Matriks yang berisi data uji
        :param weight_class (tuple): Tuple yang berisi pasangan bobot dan labelnya
        :return: Nilai prediksi label/class
        """

        # print('weight class =', weight_class)
        weight, label = weight_class
        # print('berat =', weight)
        # print('label =', label)
        # print('test data', test_data)
        distance = np.sqrt(np.sum((test_data - weight)**2, axis=1))
        idx_min = np.argmin(distance)
        # print('idx_min', idx_min)
        output = label[idx_min]
        return output

    def test_self(self, test_data, weight_class):
        weight, label = weight_class
        output = []
        for data in test_data:
            distance = np.sqrt(np.sum((data - weight) ** 2, axis=1))
            idx_min = np.argmin(distance)
            # print('idx_min', idx_min)
            output.append(label[idx_min])
        return output

def run():
    # datatest = pd.read_csv(
    #     "E:/Project/Deteksi_Masker_Project/dataset/test_1000.csv")
    # # datatest = pd.read_excel("Skripsi/Face_Mask/NewMasker/Test.xlsx")
    # data2 = datatest.iloc[:, 1:-1]
    # y_label = datatest['Class']
    # x_test = np.array(data2)
    # y_test = np.array(y_label)

    # df_bobot = pd.read_csv(
    #     "E:/Project/Deteksi_Masker_Project/dataset/bobot_lvq_9000(10-0.001).csv")

    # bobot = df_bobot.iloc[:, :-1]
    # label_bobot = df_bobot['Class']

    # bobot = np.array(bobot)
    # label_bobot = np.array(label_bobot)
    # bobot_dan_label = (bobot, label_bobot)
    # # print(bobot_dan_label)

    # # Testing
    # y_pred = LVQ.test(self=LVQ, test_data=x_test,
    #                   weight_class=bobot_dan_label)
    # # print('Label Pred: ', y_pred)
    # # print('Label True: ', y_test)
    # print('Accuracy:', accuracy_score(y_test, y_pred))
    # # print('Class', y_pred)
    # # hasil = y_pred
    
    # datatest = pd.read_excel("E:/Project/Skripsi/Face_Mask/Foto_data/test.xlsx")
    # # datatest = pd.read_excel("E:/Project/Deteksi_Masker_Project/dataset/test/test.xlsx")
    # data2 = datatest.iloc[:, 1:-1]
    # y_label = datatest['Class']
    # x_test = np.array(data2)
    # y_test = np.array(y_label)

    dataset = pd.read_csv(
        "E:/Project/Deteksi_Masker_Project/dataset/dataset_hasil/dataset_hasil2.csv")
    data = dataset.iloc[:, 1:-1]
    label = dataset['Class']

    # Pembagian data training & testing
    size = 0.3
    x_train, x_test, y_train, y_test = train_test_split(
        data, label, stratify=label, test_size=size)
    x_train = np.array(data)
    # print('x_train =', x_train)
    x_test = np.array(x_test)
    # print('x_test =', x_test)
    y_train = np.array(label)
    # print('y_train =', y_train)
    y_test = np.array(y_test)
    # print('y_test :', y_test)
    n_input = x_train.shape[1]

    n_output = len(np.unique(y_train))
    # print('Input Neuron:', n_input)
    # print('Output Neuron:', n_output)

    # LVQ1
    # Training
    alpha = [0.1, 0.01, 0.001]
    print('test_size = ', size)
    for ap in alpha:
        print('alpha =', ap)
        for epoch in range(10, 110, 10):
            lvq = LVQ(sizeInput=n_input, sizeOutput=n_output,
                      max_epoch=epoch, alpha=ap, minalpha=0.00001, decalpha=0.1)
            bobot_dan_label = lvq.train(x_train, y_train)

            # bobot = lvq.get()
            # print('Bobot: ', bobot)
            # print('Ukuran Bobot:', bobot.shape)

            # Testing
            y_pred = lvq.test_self(x_test, bobot_dan_label)
            # print('Label Pred: ', y_pred)
            # print('Label True: ', y_test)
            print('Epoch_'+str(epoch)+', Accuracy:'+str(
                  accuracy_score(y_test, y_pred)*100))
            # print('Loss =', log_loss(y_test, y_pred))
            # print('test =', y_test, 'pred', y_pred)


if __name__ == "__main__":
    run()
