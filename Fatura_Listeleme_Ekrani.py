# Form implementation generated from reading ui file 'Fatura_Listeleme.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1379, 785)
        self.FaturaTablosu = QtWidgets.QTableWidget(parent=Form)
        self.FaturaTablosu.setGeometry(QtCore.QRect(40, 80, 1301, 291))
        self.FaturaTablosu.setObjectName("FaturaTablosu")
        self.FaturaTablosu.setColumnCount(0)
        self.FaturaTablosu.setRowCount(0)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(590, 20, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(870, 420, 361, 231))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 62, 21))
        self.label_2.setObjectName("label_2")
        self.txtFaturaID = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtFaturaID.setGeometry(QtCore.QRect(160, 30, 125, 21))
        self.txtFaturaID.setObjectName("txtFaturaID")
        self.btnPdf = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnPdf.setGeometry(QtCore.QRect(150, 60, 113, 32))
        self.btnPdf.setObjectName("btnPdf")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 420, 351, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblgonderen = QtWidgets.QLabel(parent=self.groupBox_2)
        self.lblgonderen.setObjectName("lblgonderen")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblgonderen)
        self.txtGonderen = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtGonderen.setObjectName("txtGonderen")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtGonderen)
        self.txtKonu = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtKonu.setObjectName("txtKonu")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtKonu)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.txtAlici = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtAlici.setObjectName("txtAlici")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtAlici)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.btn_eposta = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btn_eposta.setObjectName("btn_eposta")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.btn_eposta)
        self.txtFaturaIDEposta = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtFaturaIDEposta.setObjectName("txtFaturaIDEposta")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtFaturaIDEposta)
        self.lblgonderen_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.lblgonderen_2.setObjectName("lblgonderen_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblgonderen_2)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_3.setGeometry(QtCore.QRect(200, 420, 261, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName("formLayout")
        self.txtFaturAraSil = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.txtFaturAraSil.setObjectName("txtFaturAraSil")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtFaturAraSil)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.btnAra = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnAra.setObjectName("btnAra")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.btnAra)
        self.btn_faturasil = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btn_faturasil.setObjectName("btn_faturasil")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.btn_faturasil)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FATURALARIM"))
        self.label.setText(_translate("Form", "E-FATURLARIM EKRANI"))
        self.groupBox.setTitle(_translate("Form", "Pdf Dönüştür"))
        self.label_2.setText(_translate("Form", "Fatura NO"))
        self.btnPdf.setText(_translate("Form", "PDF"))
        self.groupBox_2.setTitle(_translate("Form", "Mail Gönder"))
        self.lblgonderen.setText(_translate("Form", "Gonderen"))
        self.label_3.setText(_translate("Form", "Alıcı"))
        self.label_4.setText(_translate("Form", "Konu"))
        self.btn_eposta.setText(_translate("Form", "E-POSTA"))
        self.lblgonderen_2.setText(_translate("Form", "Fatura NO"))
        self.groupBox_3.setTitle(_translate("Form", "Ara/Sil"))
        self.label_5.setText(_translate("Form", "Fatura NO"))
        self.btnAra.setText(_translate("Form", "Fatura Ara"))
        self.btn_faturasil.setText(_translate("Form", "Fatura Sil"))
