# Form implementation generated from reading ui file 'Fatura_Ekrani.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Fature_Ekrani(object):
    def setupUi(self, Fature_Ekrani):
        Fature_Ekrani.setObjectName("Fature_Ekrani")
        Fature_Ekrani.resize(1154, 553)
        self.groupBox = QtWidgets.QGroupBox(parent=Fature_Ekrani)
        self.groupBox.setGeometry(QtCore.QRect(90, 50, 291, 331))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tarih = QtWidgets.QDateEdit(parent=self.groupBox)
        self.tarih.setObjectName("tarih")
        self.gridLayout.addWidget(self.tarih, 0, 1, 1, 2)
        self.txtDovizKuru = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtDovizKuru.setObjectName("txtDovizKuru")
        self.gridLayout.addWidget(self.txtDovizKuru, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.saat = QtWidgets.QTimeEdit(parent=self.groupBox)
        self.saat.setObjectName("saat")
        self.gridLayout.addWidget(self.saat, 1, 1, 1, 2)
        self.cmbParaBirimi = QtWidgets.QComboBox(parent=self.groupBox)
        self.cmbParaBirimi.setCurrentText("")
        self.cmbParaBirimi.setObjectName("cmbParaBirimi")
        self.cmbParaBirimi.addItem("")
        self.cmbParaBirimi.addItem("")
        self.cmbParaBirimi.addItem("")
        self.gridLayout.addWidget(self.cmbParaBirimi, 2, 2, 1, 1)
        self.cmbFaturaTipi = QtWidgets.QComboBox(parent=self.groupBox)
        self.cmbFaturaTipi.setObjectName("cmbFaturaTipi")
        self.cmbFaturaTipi.addItem("")
        self.gridLayout.addWidget(self.cmbFaturaTipi, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Fature_Ekrani)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 50, 291, 331))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.txttc = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txttc.setText("")
        self.txttc.setObjectName("txttc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txttc)
        self.txtunvan = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtunvan.setObjectName("txtunvan")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtunvan)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.txtad = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtad.setObjectName("txtad")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtad)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.txtsoyad = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtsoyad.setObjectName("txtsoyad")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtsoyad)
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.txtvergidairesi = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtvergidairesi.setObjectName("txtvergidairesi")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtvergidairesi)
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.cmbulke = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.cmbulke.setObjectName("cmbulke")
        self.cmbulke.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cmbulke)
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.txtadres = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.txtadres.setObjectName("txtadres")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtadres)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=Fature_Ekrani)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 430, 291, 103))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_Ekle = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btn_Ekle.setObjectName("btn_Ekle")
        self.gridLayout_2.addWidget(self.btn_Ekle, 0, 0, 1, 1)
        self.btn_Temizle = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btn_Temizle.setObjectName("btn_Temizle")
        self.gridLayout_2.addWidget(self.btn_Temizle, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=Fature_Ekrani)
        self.groupBox_4.setGeometry(QtCore.QRect(730, 50, 341, 331))
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.txtUrunBilgisi = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.txtUrunBilgisi.setObjectName("txtUrunBilgisi")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtUrunBilgisi)
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.txtUrunAdet = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.txtUrunAdet.setObjectName("txtUrunAdet")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtUrunAdet)
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_16)
        self.txtBirimFiyati = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.txtBirimFiyati.setObjectName("txtBirimFiyati")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBirimFiyati)
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_17)
        self.txtUrunBilgisi_5 = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.txtUrunBilgisi_5.setReadOnly(True)
        self.txtUrunBilgisi_5.setObjectName("txtUrunBilgisi_5")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtUrunBilgisi_5)
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.lblTutar = QtWidgets.QLabel(parent=self.groupBox_4)
        self.lblTutar.setObjectName("lblTutar")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lblTutar)
        self.btnHesapla = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.btnHesapla.setObjectName("btnHesapla")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.btnHesapla)

        self.retranslateUi(Fature_Ekrani)
        self.cmbParaBirimi.setCurrentIndex(-1)
        self.cmbFaturaTipi.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Fature_Ekrani)

    def retranslateUi(self, Fature_Ekrani):
        _translate = QtCore.QCoreApplication.translate
        Fature_Ekrani.setWindowTitle(_translate("Fature_Ekrani", "E-FATURA"))
        self.groupBox.setTitle(_translate("Fature_Ekrani", "FATURA BİLGİLERİ"))
        self.label_2.setText(_translate("Fature_Ekrani", "Düzenleme Tarihi"))
        self.label_4.setText(_translate("Fature_Ekrani", "Döküman Para Birimi"))
        self.label_5.setText(_translate("Fature_Ekrani", "Döviz Kuru"))
        self.label.setText(_translate("Fature_Ekrani", "Düzenleme Saati"))
        self.cmbParaBirimi.setItemText(0, _translate("Fature_Ekrani", "Euro"))
        self.cmbParaBirimi.setItemText(1, _translate("Fature_Ekrani", "Dolar"))
        self.cmbParaBirimi.setItemText(2, _translate("Fature_Ekrani", "TL"))
        self.cmbFaturaTipi.setItemText(0, _translate("Fature_Ekrani", "Satış"))
        self.label_6.setText(_translate("Fature_Ekrani", "Fatura Tipi"))
        self.groupBox_2.setTitle(_translate("Fature_Ekrani", "ALICI BİLGİLERİ"))
        self.label_7.setText(_translate("Fature_Ekrani", "VKN/TCKN "))
        self.txttc.setInputMask(_translate("Fature_Ekrani", "00000000000"))
        self.label_8.setText(_translate("Fature_Ekrani", "Unvan"))
        self.label_9.setText(_translate("Fature_Ekrani", "Adı"))
        self.label_10.setText(_translate("Fature_Ekrani", "Soyadı"))
        self.label_11.setText(_translate("Fature_Ekrani", "Vergi Dairesi"))
        self.cmbulke.setItemText(0, _translate("Fature_Ekrani", "Türkiye"))
        self.label_12.setText(_translate("Fature_Ekrani", "Ülke"))
        self.label_13.setText(_translate("Fature_Ekrani", "Adres"))
        self.btn_Ekle.setText(_translate("Fature_Ekrani", "Ekle"))
        self.btn_Temizle.setText(_translate("Fature_Ekrani", "Temizle"))
        self.groupBox_4.setTitle(_translate("Fature_Ekrani", "ÜRÜN BİLGİLERİ"))
        self.label_3.setText(_translate("Fature_Ekrani", "Ürün Bilgisi"))
        self.label_14.setText(_translate("Fature_Ekrani", "Ürün Adet"))
        self.label_16.setText(_translate("Fature_Ekrani", "Birim Fiyatı"))
        self.label_17.setText(_translate("Fature_Ekrani", "KDV "))
        self.txtUrunBilgisi_5.setText(_translate("Fature_Ekrani", "%18"))
        self.label_15.setText(_translate("Fature_Ekrani", "Toplam Tutar:"))
        self.lblTutar.setText(_translate("Fature_Ekrani", "----"))
        self.btnHesapla.setText(_translate("Fature_Ekrani", "Hesapla"))
