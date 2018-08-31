#from telnetlib import Telnet
from vxi11 import Instrument as Telnet
import time

# Do not reopen an already connected instance.
import sys

class connection(Telnet):
    """docstring for scpi."""
    def __init__(self, __host):
        self.__host=__host
        #self.__port=__port
        Telnet.__init__(self,__host)

    def get_host(self):
        return self.__host


    def set_scpi(self,object,e,std,timer=3,JUST_READ=False):
        "Retorna un comando SCPI efectudado o un error"
        try:
            if JUST_READ:
                return object.ask(std+'\n', encoding='utf-8')
            else:
                object.write(std, encoding='utf-8')
            #object.write(std+"\n")
            #print object.read_until("\n",1)
            #object.read_some()
            #print object.read_all()
            #print object.interact()
            #print object.read_some()
        except Exception as e:
            return e
        else:
            print "Command: ",std,"Perfomed Correctly."

            if timer ==None:
                timer=3
            time.sleep(timer)

    def __verify(self,object,e):
        object.write("\n")
        try:
            object.read_until("SCPI> ",3)
        except Exception as e:
            print "Connection have Failed :",e
            return e
        else:
            print "\n FieldBox Tested"


    #def set_scpi(self,object,std="gossip",Pass="gossip(GSM"):
        #object.read_until("login: ")
        #object.write(std + "\n")

        #if Pass:
            #object.read_until("Password: ")
            #object.write(Pass + "\n")

        #object.write("ls\n")
        #object.write("exit\n")
        #print object.read_all()
