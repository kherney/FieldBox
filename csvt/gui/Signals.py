# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/Signals.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(934, 455)
        self.plotSignal = QwtPlot(Dialog)
        self.plotSignal.setGeometry(QtCore.QRect(10, 10, 801, 431))
        self.plotSignal.setObjectName(_fromUtf8("plotSignal"))
        self.xSignal = QtGui.QPushButton(Dialog)
        self.xSignal.setGeometry(QtCore.QRect(830, 40, 89, 27))
        self.xSignal.setObjectName(_fromUtf8("xSignal"))
        self.ySignal = QtGui.QPushButton(Dialog)
        self.ySignal.setGeometry(QtCore.QRect(830, 70, 89, 27))
        self.ySignal.setObjectName(_fromUtf8("ySignal"))
        self.FFT = QtGui.QPushButton(Dialog)
        self.FFT.setGeometry(QtCore.QRect(830, 250, 89, 27))
        self.FFT.setObjectName(_fromUtf8("FFT"))
        self.IFFT = QtGui.QPushButton(Dialog)
        self.IFFT.setGeometry(QtCore.QRect(830, 280, 89, 27))
        self.IFFT.setObjectName(_fromUtf8("IFFT"))
        self.btnClear = QtGui.QPushButton(Dialog)
        self.btnClear.setGeometry(QtCore.QRect(830, 390, 89, 27))
        self.btnClear.setObjectName(_fromUtf8("btnClear"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.xSignal.setText(_translate("Dialog", "X signal", None))
        self.ySignal.setText(_translate("Dialog", "Y signal", None))
        self.FFT.setText(_translate("Dialog", "FFT", None))
        self.IFFT.setText(_translate("Dialog", "IFFT", None))
        self.btnClear.setText(_translate("Dialog", "Clear", None))

from PyQt4.Qwt5 import QwtPlot
