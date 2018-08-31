# Author: Kevin Herney
# Feeling free to change anything

import csv
from PyQt4 import uic,QtGui,QtCore,Qwt5
from PyQt4.Qwt5 import QwtPlot
import numpy as np
global Ui_mainDialog,QtBaseClass
try:
    import os
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "gui/Signals.ui"
    abs_uifile_path = os.path.join(script_dir,rel_path)
    rel_path = "gui/Signals.py"
    abs_pyfile_path = os.path.join(script_dir,rel_path)
    file=open(abs_pyfile_path, 'wt')
except Exception as e:
    raise "NO se encentra archivo: ",e
else:
    Ui_mainDialog,QtBaseClass = uic.loadUiType(abs_uifile_path, from_imports=False, resource_suffix='_rc')
    uic.compileUi(abs_uifile_path, file, execute=False, indent=4, pyqt3_wrapper=False, from_imports=False, resource_suffix='_rc')



class dialogSignal(QtBaseClass,Ui_mainDialog):
    """docstring for dialogSignal."""
    def __init__(self):
        QtBaseClass.__init__(self)
        self.setupUi(self)
        self.fs=4000
        self.t=self.__arrayss('toneTime_t.csv')
        self.x=self.__arrayss('toneTime_x.csv')
        self.y=self.__arrayss("toneFrecuency_y.csv")
        self.f=self.__arrayss("toneFrecuency_f.csv")

    def __arrayss(self,str):
        results = []
        with open(str,'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                #print ', '.join(row)
                results.append(row)
        results=[float(n) for n in results[0][0].split(',')]
        return results

    def Xsignal(self):
        """Signal source perfom in matalab"""
        self.plotSignal.setTitle("Signal X")
        self.plotSignal.setAxisTitle(QwtPlot.xBottom, 'Time')
        self.plotSignal.setAxisTitle(QwtPlot.yLeft, 'Y(time)')

        curve = Qwt5.QwtPlotCurve('XSignal')
        curve.setData(self.t,self.x)
        print "long de x = ",len(self.x)
        curve.attach(self.plotSignal)
        self.plotSignal.replot()

    def Ysignal(self):
        """FFT perfom in Matlab"""
        self.plotSignal.setTitle('Signal Y')
        self.plotSignal.setAxisTitle(QwtPlot.xBottom,'Frecuency')
        self.plotSignal.setAxisTitle(QwtPlot.yLeft,'Power Spectral')

        curve=Qwt5.QwtPlotCurve("Signal Y")
        curve.setData(self.f,self.y)
        curve.attach(self.plotSignal)
        self.plotSignal.replot()

        print "long de y = ",len(self.y)

    def clearS(self):
        self.plotSignal.clear()
        self.plotSignal.setTitle('')
        self.plotSignal.setAxisTitle(QwtPlot.xBottom,'')
        self.plotSignal.setAxisTitle(QwtPlot.yLeft,'')
        self.plotSignal.replot()

    def FFt(self):
        """
            Fs=4000
            Fc=200
            df=0.0005
            Transformada de Fourrier de una signal de
            Matlab en archivo CSV.
        """
        global maxS,fft_y2
        self.plotSignal.setTitle("FFT Transform")
        self.plotSignal.setAxisTitle(QwtPlot.xBottom,"X Transform")
        self.plotSignal.setAxisTitle(QwtPlot.yLeft,"y Transform")

        #Perfom FFT
        fft=np.fft.fft(self.x, n=None, axis=-1, norm=None)
        # Normal operation and non-negative values
        #fft_y= [n/max(fft_y) for n in fft_y]
        maxS=[abs(n) for n in fft]
        maxS=max(maxS)
        #Normalizacion
        fft_y2=[float(abs(n)/max(abs(fft))) for n in fft]
        #Just the positive spectrum (fs/2)
        fft_y = fft_y2[0:(len(fft_y2)+1)/2]
        fft_x2=np.fft.fftfreq(len(fft), d=0.00025) #2/fs(La Mitad #fft_y= [n/max(fft_y) for n in fft_y]d el espectro)
        fft_x=np.arange(0,self.fs,(self.fs/2)/len(fft_y))#df 2/fs 'cause's just the positive spectrum
        curve = Qwt5.QwtPlotCurve("FFT curve")

        curve.setData(fft_x,fft_y)
        curve.attach(self.plotSignal)
        self.plotSignal.replot()

    def IFFt(self):
        """
            Fs=4000
            dt=0.00025
            Fc=200
            Transformada de Fourrier de una signal de
            Matlab en archivo CSV.
        """
        self.FFt()

        self.clearS()

        fft_y1=[maxS*n for n in fft_y2]
        x=np.fft.ifft(fft_y1, n=None, axis=-1, norm=None)
        #print "long t= ",len(self.t),"Long x= ",len(x)
        t=np.arange(0,float(x.size)/self.fs,1.0/self.fs)
        #print "data t= ",self.t," \n data x= ",t

        curve=Qwt5.QwtPlotCurve("IFFT Signal")
        curve.setData(t,np.real(x))
        curve.attach(self.plotSignal)


        mY=Qwt5.QwtPlotMarker()
        mY.setLabel(Qwt5.QwtText('y=0'))
        #mY.setLabelAlignment()
        self.plotSignal.replot()


    def GUIactions(self):
        self.xSignal.clicked.connect(self.Xsignal)
        self.ySignal.clicked.connect(self.Ysignal)
        self.btnClear.clicked.connect(self.clearS)
        self.FFT.clicked.connect(self.FFt)
        self.IFFT.clicked.connect(self.IFFt)


if __name__ == '__main__':
    import sys
    App=QtGui.QApplication(sys.argv)
    S=dialogSignal()
    S.GUIactions()
    S.show()
    App.exec_()
