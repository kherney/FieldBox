#from linked import  telnetConnect as T
from linked.telnetConnect import connection
from management.calFile import CalFile
import argparse
import time
import datetime


def main():
    """ """
    try:
        #Port 5024 with CLI mode libtelnet
        cn=connection("80.0.0.3")

        fl=CalFile()
        print 'Connecting to', cn.get_host()
    except Exception as e:
        #print 'Failed Connect to', cn.get_host()
        print e
        cn=None
    else:
        print "Connection successful"
        try:
            cn.set_scpi(cn,Exception,"*RST",7)
            fl.recall(cn)
            cn.set_scpi(cn,Exception,"CALC:PAR:COUN 2",2)
            cn.set_scpi(cn,Exception,"CALC:PAR2:DEF S21",2)
            cn.set_scpi(cn,Exception,"CALC:PAR2:SEL",1)
            cn.set_scpi(cn,Exception,"CALC:FORMat MLIN",1)
            cn.set_scpi(cn,Exception,"DISPlay:WINDow:TRAC2:Y:AUTO",1)
            cn.set_scpi(cn,Exception,"CALC:PAR1:SEL",1)
            cn.set_scpi(cn,Exception,"CALC:FORMat MLOG",1)
            cn.set_scpi(cn,Exception,"DISPlay:WINDow:TRAC1:Y:AUTO",1)
            cn.set_scpi(cn,Exception,"SOUR:POW -15",1)
            cn.set_scpi(cn,Exception,":SOURce:POWer?",1,True)


        except Exception as e:
            print "Halgo ha Fallado:",e

    finally:
        if cn:
            cn.close()
            print "\n\n Finalized Script"
        else:
            print "Review your configuration or connection"

if __name__== "__main__":

    """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args()
    print args.accumulate(args.integers)
    """
    main()
