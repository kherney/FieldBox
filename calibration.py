from linked.telnetConnect import connection


def mechanical(self):
    pass
def ResponseCal(self):
    pass

def main():
    try:
        cn=connection("192.168.0.41")

        print 'Connecting to', cn.get_host()
    except Exception as e:
        #print 'Failed Connect to', cn.get_host()
        print e
        cn=None
    else:
        print "Connection successful "
        cn.set_scpi(cn)

    finally:
        if cn:
            cn.close()
            print "Finalized Script"
        else:
            print "Review your configuration or connection"

if __name__ == '__main__':
    main()
