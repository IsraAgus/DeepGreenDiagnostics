# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V_Chooser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TrainFiles(object):
    def setupUi(self, TrainFiles):
        TrainFiles.setObjectName("TrainFiles")
        TrainFiles.resize(611, 339)
        self.V1F2 = QtWidgets.QFrame(TrainFiles)
        self.V1F2.setGeometry(QtCore.QRect(0, 90, 611, 80))
        self.V1F2.setAutoFillBackground(False)
        self.V1F2.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V1F2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V1F2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V1F2.setObjectName("V1F2")
        self.V1F2E1_Ingresa = QtWidgets.QLabel(self.V1F2)
        self.V1F2E1_Ingresa.setEnabled(True)
        self.V1F2E1_Ingresa.setGeometry(QtCore.QRect(40, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E1_Ingresa.setFont(font)
        self.V1F2E1_Ingresa.setObjectName("V1F2E1_Ingresa")
        self.V5_DIR_IMGS = QtWidgets.QPushButton(self.V1F2)
        self.V5_DIR_IMGS.setGeometry(QtCore.QRect(530, 20, 51, 27))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V5_DIR_IMGS.setFont(font)
        self.V5_DIR_IMGS.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.V5_DIR_IMGS.setObjectName("V5_DIR_IMGS")
        self.V1F2_2 = QtWidgets.QFrame(self.V1F2)
        self.V1F2_2.setGeometry(QtCore.QRect(620, 70, 641, 80))
        self.V1F2_2.setAutoFillBackground(False)
        self.V1F2_2.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.V1F2_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.V1F2_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.V1F2_2.setObjectName("V1F2_2")
        self.V1F2E1_Ingresa_2 = QtWidgets.QLabel(self.V1F2_2)
        self.V1F2E1_Ingresa_2.setEnabled(True)
        self.V1F2E1_Ingresa_2.setGeometry(QtCore.QRect(40, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E1_Ingresa_2.setFont(font)
        self.V1F2E1_Ingresa_2.setObjectName("V1F2E1_Ingresa_2")
        self.V1F2B1_Directorio_2 = QtWidgets.QPushButton(self.V1F2_2)
        self.V1F2B1_Directorio_2.setGeometry(QtCore.QRect(530, 20, 51, 27))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V1F2B1_Directorio_2.setFont(font)
        self.V1F2B1_Directorio_2.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.V1F2B1_Directorio_2.setObjectName("V1F2B1_Directorio_2")
        self.V1F2E2_Path_2 = QtWidgets.QLabel(self.V1F2_2)
        self.V1F2E2_Path_2.setGeometry(QtCore.QRect(150, 20, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E2_Path_2.setFont(font)
        self.V1F2E2_Path_2.setAlignment(QtCore.Qt.AlignCenter)
        self.V1F2E2_Path_2.setObjectName("V1F2E2_Path_2")
        self.V1F2E2_Path = QtWidgets.QLabel(self.V1F2)
        self.V1F2E2_Path.setGeometry(QtCore.QRect(130, 20, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E2_Path.setFont(font)
        self.V1F2E2_Path.setAlignment(QtCore.Qt.AlignCenter)
        self.V1F2E2_Path.setObjectName("V1F2E2_Path")
        self.Chooser_F1 = QtWidgets.QFrame(TrainFiles)
        self.Chooser_F1.setGeometry(QtCore.QRect(0, 0, 721, 91))
        self.Chooser_F1.setAutoFillBackground(False)
        self.Chooser_F1.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.Chooser_F1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Chooser_F1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Chooser_F1.setObjectName("Chooser_F1")
        self.chooser_preparar = QtWidgets.QPushButton(self.Chooser_F1)
        self.chooser_preparar.setEnabled(True)
        self.chooser_preparar.setGeometry(QtCore.QRect(220, 20, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chooser_preparar.setFont(font)
        self.chooser_preparar.setMouseTracking(True)
        self.chooser_preparar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.chooser_preparar.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.chooser_preparar.setObjectName("chooser_preparar")
        self.Chooser_NN = QtWidgets.QFrame(TrainFiles)
        self.Chooser_NN.setGeometry(QtCore.QRect(0, 170, 611, 71))
        self.Chooser_NN.setAutoFillBackground(False)
        self.Chooser_NN.setStyleSheet("background-color: rgb(216, 223, 234);\n"
"border: rgb(216, 223, 234);")
        self.Chooser_NN.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Chooser_NN.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Chooser_NN.setObjectName("Chooser_NN")
        self.V1F2E1_Ingresa_3 = QtWidgets.QLabel(self.Chooser_NN)
        self.V1F2E1_Ingresa_3.setEnabled(True)
        self.V1F2E1_Ingresa_3.setGeometry(QtCore.QRect(30, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E1_Ingresa_3.setFont(font)
        self.V1F2E1_Ingresa_3.setObjectName("V1F2E1_Ingresa_3")
        self.V5_DIR_CSV = QtWidgets.QPushButton(self.Chooser_NN)
        self.V5_DIR_CSV.setGeometry(QtCore.QRect(530, 20, 51, 27))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.V5_DIR_CSV.setFont(font)
        self.V5_DIR_CSV.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.V5_DIR_CSV.setObjectName("V5_DIR_CSV")
        self.V1F2E2_Path_3 = QtWidgets.QLabel(self.Chooser_NN)
        self.V1F2E2_Path_3.setGeometry(QtCore.QRect(150, 30, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.V1F2E2_Path_3.setFont(font)
        self.V1F2E2_Path_3.setAlignment(QtCore.Qt.AlignCenter)
        self.V1F2E2_Path_3.setObjectName("V1F2E2_Path_3")
        self.Param_input = QtWidgets.QFrame(TrainFiles)
        self.Param_input.setGeometry(QtCore.QRect(0, 240, 611, 101))
        self.Param_input.setAutoFillBackground(False)
        self.Param_input.setStyleSheet("background-color: rgb(1, 118, 180);\n"
"border:rgb(1, 118, 180);")
        self.Param_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Param_input.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Param_input.setObjectName("Param_input")
        self.Ingresa_it = QtWidgets.QLabel(self.Param_input)
        self.Ingresa_it.setEnabled(True)
        self.Ingresa_it.setGeometry(QtCore.QRect(10, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(True)
        font.setWeight(75)
        self.Ingresa_it.setFont(font)
        self.Ingresa_it.setObjectName("Ingresa_it")
        self.lineEdit = QtWidgets.QLineEdit(self.Param_input)
        self.lineEdit.setGeometry(QtCore.QRect(250, 40, 91, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"font: 18pt \"Comfortaa\";")
        self.lineEdit.setObjectName("lineEdit")
        self.chooser_enviar = QtWidgets.QPushButton(self.Param_input)
        self.chooser_enviar.setEnabled(True)
        self.chooser_enviar.setGeometry(QtCore.QRect(450, 20, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chooser_enviar.setFont(font)
        self.chooser_enviar.setMouseTracking(True)
        self.chooser_enviar.setStyleSheet("font: 18pt \"Comfortaa\";\n"
"background-color: rgb(213, 213, 213);")
        self.chooser_enviar.setObjectName("chooser_enviar")

        self.retranslateUi(TrainFiles)
        QtCore.QMetaObject.connectSlotsByName(TrainFiles)

    def retranslateUi(self, TrainFiles):
        _translate = QtCore.QCoreApplication.translate
        TrainFiles.setWindowTitle(_translate("TrainFiles", "Archivos para entrenar"))
        self.V1F2E1_Ingresa.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Imágenes:</span></p></body></html>"))
        self.V5_DIR_IMGS.setText(_translate("TrainFiles", "..."))
        self.V1F2E1_Ingresa_2.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Carpeta:</span></p></body></html>"))
        self.V1F2B1_Directorio_2.setText(_translate("TrainFiles", "..."))
        self.V1F2E2_Path_2.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" color:#ffffff;\"></span></p></body></html>"))
        self.V1F2E2_Path.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" color:#ffffff;\"></span></p></body></html>"))
        self.chooser_preparar.setText(_translate("TrainFiles", "Preparar imágenes"))
        self.V1F2E1_Ingresa_3.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">Archivo CSV:</span></p></body></html>"))
        self.V5_DIR_CSV.setText(_translate("TrainFiles", "..."))
        self.V1F2E2_Path_3.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" color:#ffffff;\"></span></p></body></html>"))
        self.Ingresa_it.setText(_translate("TrainFiles", "<html><head/><body><p><span style=\" font-family:\'.SF NS Text\'; font-size:18pt; font-weight:400; color:#ffffff;\">Ingresa no de Iteraciones:</span></p></body></html>"))
        self.lineEdit.setText(_translate("TrainFiles", "1"))
        self.chooser_enviar.setText(_translate("TrainFiles", "Enviar"))

