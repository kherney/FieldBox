import datetime as dt
import numpy as np
from PyQt4.Qwt5 import *
from PyQt4 import Qwt5

def btnOpen(object,scpi):
    scpi.open()
    object.log.appendPlainText("{} Connection established".format(dt.datetime.now().strftime("%d-%m %H:%M")))

def btnClose(object,scpi):
    try:
        scpi.close()
    except Exception as e:
        object.log.appendPlainText(str(e))
    else:
        object.log.clear()
        object.log.appendPlainText("{} Connection closed".format(dt.datetime.now().strftime("%d-%m %H:%M")))

def btnRangeFreq(object,scpi):

    inicio=object.iniFreq.text()
    fin=object.endFreq.text()
    __inicio,__fin=__parseUnit(inicio,fin)
    scpi.set_scpi(scpi,Exception,"FREQ:STAR {}".format(__inicio),1)
    scpi.set_scpi(scpi,Exception,"FREQ:STOP {}".format(__fin),1)
    object.log.appendPlainText("Range Frecuency between {}Hz - {}Hz".format(inicio,fin))
    scpi.set_scpi(scpi,Exception,"INIT:CONT 1",1)

def variablePower(object,scpi):
    #Max power +3 dBm
    #min power -45 dBm
    scpi.set_scpi(scpi,Exception,"SOUR:POW {}".format(str(object.powerStep.value())),1)
def initTrace_ph(object,scpi):

    scpi.set_scpi(scpi,Exception,"INST:SEL 'NA'",1)
    scpi.set_scpi(scpi,Exception,"CALC:PAR:COUN 1",1)
    scpi.set_scpi(scpi,Exception,"CALC:PAR1:DEF S21",1)
    scpi.set_scpi(scpi,Exception,"CALC:PAR1:SEL",1)
    scpi.set_scpi(scpi,Exception,"CALC:FORMat PHAS",1)
    scpi.set_scpi(scpi,Exception,"INIT:CONT 0",1)

def saveTrace_ph(object,scpi):
    global points
    scpi.set_scpi(scpi,Exception,"INIT:CONT 0",1)
    rawAs=scpi.set_scpi(scpi,Exception,"CALC:DATA:FDATa?",3,True)
    rawAs=''.join([x.encode('UTF8') for x in rawAs]).split(',')
    points=[float(x) for x in rawAs]

    object.phasePlot.setTitle('Real Screenshot measurament')

    object.phasePlot.setAxisTitle(QwtPlot.xBottom, 'x -->')
    object.phasePlot.setAxisTitle(QwtPlot.yLeft, 'y -->')
    object.phasePlot.enableAxis(object.phasePlot.xBottom)

    curve = Qwt5.QwtPlotCurve("curve1")
    curve.setTitle("HOla")
    x=np.arange(start=0.0, stop=201.0, step=1, dtype=None)
    curve.setData(x,points)

    curve.attach(object.phasePlot)
    object.phasePlot.replot()

def clearTrace(object,scpi):
    object.phasePlot.clear()
    object.phasePlot.replot()

def IFFT(object,scpi):
    curve_P = Qwt5.QwtPlotCurve("curve2")
    curve_P.setTitle("Prueba")
    t=np.arange(0,100/2e6,1/2e6)
    #t=np.arange(100)
    s = np.fft.ifft(points,201)
    curve_P.setData(t,abs(s[0:100].real))
    curve_P.attach(object.phasePlot)
    object.phasePlot.replot()

def FFT(object,scpi):
    curve_P = Qwt5.QwtPlotCurve("curve2")
    curve_P.setTitle("Prueba")
    x=np.arange(start=0.0, stop=250.0, step=1, dtype=None)
    sp=np.fft.fft(np.cos(x), n=None, axis=-1, norm=None)
    n=x.size
    freq=np.fft.fftfreq=(n)
    curve_P.setData(freq,sp.real)
    curve_P.attach(object.phasePlot)
    object.phasePlot.replot()

def prueba(object,scpi):
    curve_P = Qwt5.QwtPlotCurve("curve2")
    curve_P.setTitle("Prueba")
    x=np.arange(start=0.0, stop=250.0, step=0.1, dtype=None)
    curve_P.setData(x,np.cos(x))
    curve_P.attach(object.phasePlot)
    object.phasePlot.replot()



def __parseUnit(*args):
    unidades={'G':'E9','M':"E6",'K':"E3"}
    A=[]
    result=[]
    p=0
    for i in args:
        for j in i:
            if str(j) in str(unidades.keys()):
                j=unidades.get(str(j))
            A.append(str(j))
        result.append(''.join(A))
        del A[:]
    return tuple(result)
