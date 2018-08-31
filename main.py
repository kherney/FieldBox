from linked.telnetConnect import connection
from PyQt4 import QtCore,QtGui,uic
from port import *

global Ui_MainWindow,QtBaseClass
IDN_STRING="Agilent Technologies,N9915A,MY53103694,A.07.52,2014-07-01.13:10"

try:
    import os
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "gui/FieldBox.ui"
    abs_uifile_path = os.path.join(script_dir,rel_path)
    rel_path = "gui/fieldbox.py"
    abs_pyfile_path = os.path.join(script_dir,rel_path)
    file=open(abs_pyfile_path, 'wt')
except Exception as e:
    print e
else:
    uic.compileUi(abs_uifile_path, file, execute=False, indent=4, pyqt3_wrapper=False, from_imports=False, resource_suffix='_rc')
    Ui_MainWindow, QtBaseClass = uic.loadUiType(abs_uifile_path, from_imports=False, resource_suffix='_rc')


class apple(QtBaseClass,Ui_MainWindow):
    """app"""
    def __init__(self):
        #super(, self).__init__()(
        QtBaseClass.__init__(self)
        self.setupUi(self)
        try:
            self.cn=connection("80.0.0.3")
            #self.log.appendPlainText ('Connecting to {}'.format(self.cn.get_host()))
            self.cn.set_scpi(self.cn,Exception,"*RST",1)
            self.state=self.cn.set_scpi(self.cn,Exception,"*IDN?",1,IDN_STRING)
            if not self.state:
                raise "Error en la conexion"
        except Exception as e:
            self.log.appendPlainText(str(e))
        else:
            self.log.appendPlainText(self.state)

    def CustomUI(self):
        inst.btnOpen.clicked.connect(lambda: btnOpen(inst,inst.cn))
        inst.btnclose.clicked.connect(lambda: btnClose(inst,inst.cn))
        inst.setFreq.clicked.connect(lambda: btnRangeFreq(inst,inst.cn))
        inst.btnpwstep.clicked.connect(lambda: variablePower(inst,inst.cn))
        inst.btnPhase.clicked.connect(lambda: initTrace_ph(inst,inst.cn))
        inst.btnMeasurePh.clicked.connect(lambda: saveTrace_ph(inst,inst.cn))
        inst.btnClear.clicked.connect(lambda: clearTrace(inst,inst.cn))
        inst.btnPrueba.clicked.connect(lambda: prueba(inst,inst.cn))
        inst.btnFFT.clicked.connect(lambda: FFT(inst,inst.cn))
        inst.btnIFFT.clicked.connect(lambda: IFFT(inst,inst.cn))


if __name__ == '__main__':
    import sys
    app=QtGui.QApplication(sys.argv)
    inst=apple()
    inst.CustomUI()
    inst.show()
    app.exec_()
