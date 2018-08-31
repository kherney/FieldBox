import sys
import time
import datetime

class CalFile(object):
    """
    #Guarda una IMagen
        MMEM:STOR:IMAG "my.png"
    #Selecciona el tipo de disco
        :MMEMory:CDIRectory "[USBDISK]:"
        :MMEMory:CDIRectory?
        :MMEMory:CDIRectory "[INTERNAL]:\RadarTest"
    #Todos los archivos de de la raiz
        MMEMory:STORe:STATe "MyStateFile2.sta"

        :MMEMory:CATalog? "[INTERNAL]:\RadarTest\"
    #crea un directorio
        :MMEMory:MDIRectory "[INTERNAL]:\RadarTes\"
        :MMEMory:MDIRectory "[USBDISK]:\RadarTes\"
    #Elimina un directorio
        :MMEMory:RDIRectory "RadarTest"
    #Copia un aechivo de un lugar a otro <source>,<new_place>
        :MMEMory:COPY "[INTERNAL]:\my.png","[USBDISK]:\RadarTes\"

        :MMEMory:MDIRectory "[USBDISK]:\RadarTes\"
        :MMEMory:COPY "[INTERNAL]:\RadarTest","[USBDISK]:\RadarTest"
    #Rename a existing FIle
        :MMEMory:MOVE "[USBDISK]:\RadarTes\my.png","[USBDISK]:\RadarTes\my2.png\"
    #REmover un archivo desde un directorio dado.
        :MMEMory:DELete "my.png","[INTERNAL]:"

    """
    def __init__(self,freqRange=None,sParam=None,ifBW=None,resolution=None):
        super(CalFile, self).__init__()
        self.__freqRange=freqRange
        self.__sParam=sParam
        self.__ifBW=ifBW
        self.__resolution=resolution

    def recall(self,object,name=False):
        """
        retorna Carga una configuracion determinada
        Default CAL_IF30K_0.8-9GHZ_808P_S12.sta
        """
        if not name:
            object.set_scpi(object,Exception,":MMEMory:CDIRectory '[INTERNAL]:\RadarTest\'",1)
            object.set_scpi(object,Exception,"MMEMory:LOAD:STATe 'CAL_IF30K_0.8-9GHZ_808P_S12.sta'",10)
            print "Calibracion y configuracion CAL_IF30K_0.8-9GHZ_808P_S12.sta cargada al instrumento"


    def exportData(self,object,name,typeF):
        """
        Retorna un archivo CSV,PNG,CONF (typeF) de la medicion,PNG actual o conf
        to Create a DIR.
        :MMEMory:MDIRectory "[INTERNAL]:\RadarTest\"
        :MMEMory:MDIRectory "[INTERNAL]:\RadarTest\PNG"
        :MMEMory:MDIRectory "[INTERNAL]:\RadarTest\CSV"
        :MMEMory:MDIRectory "[INTERNAL]:\RadarTest\STATE"
        """
        #object.set_scpi(object,Exception,":MMEMory:CDIRectory '[INTERNAL]:'",1)
        if typeF=="PNG":

            object.set_scpi(object,Exception,":MMEMory:CDIRectory '[INTERNAL]:\RadarTest\PNG'",1)
            object.set_scpi(object,Exception,"MMEM:STOR:IMAG '{}-{}'".format(name,datetime.datetime.now().strftime("%y-%m-%d--%H-%M")),1)
        elif typeF=="CONF":
            object.set_scpi(object,Exception,":MMEMory:CDIRectory '[INTERNAL]:\RadarTest\STATE'",1)
            object.set_scpi(object,Exception,"MMEM:STOR:STATe '{}-{}'".format(name,datetime.datetime.now().strftime("%y-%m-%d--%H-%M")),1)
        elif typeF=="CSV":
            object.set_scpi(object,Exception,":MMEMory:CDIRectory '[INTERNAL]:\RadarTest\CSV'",1)
            object.set_scpi(object,Exception,"MMEM:STOR:FDAT '{}-{}'".format(name,datetime.datetime.now().strftime("%y-%m-%d--%H-%M")),1)

        print "{} {}-{} Guardado sastisfactoriamente".format(typeF,name,datetime.datetime.now().strftime("%y-%m-%d--%H-%M"))

    def trasnfertoUSB(self,object,exist=True):
        """
        Retorna el directorio RadarTest [INTERNAL] a [USB]
        """
        if exist:
            object.set_scpi(object,Exception,":MMEMory:MDIRectory '[USBDISK]:\RadarTest-{}'".format(datetime.datetime.now().strftime("%y-%m-%d--%H-%M")),1)
            object.set_scpi(object,Exception,":MMEMory:COPY '[INTERNAL]:\RadarTest','[USBDISK]:\RadarTest-{}'".format(datetime.datetime.now().strftime("%y-%m-%d--%H-%M")),1)
        else:
            object.set_scpi(object,Exception,":MMEMory:COPY '[INTERNAL]:\RadarTest','[USBDISK]:\RadarTest-{}'".format(datetime.datetime.now().strftime("%y-%m-%d--%H-%M")),1)


    def __find(self):
        """
        Metodo Privado. Verificar si el fichero .stat se encuentra en el directorio
        de FieldBox. PUede ser el nombre del archivo a buscar o
        con la configuracion instanciada en el objeto CalFile.
        """
        pass

    def __isIt(self,object,File):
        """
        Retorna un valor tipo Bool si el fichero pasado como argumento de
        la funcion se encuentra en el directoorio de FieldBox
        """
        pass
