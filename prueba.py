from management.calFile import CalFile

#f=CalFile("freqRange", "sParam", "ifBW", "resolution")
def validate (o):
    try:
        y=2/2
        if y==1:
            return Exception("we don't like you, Robert")
            raise Exception("we don't like you, Robert")
        print "pOINT 2"
        return 3
    except Exception as e:
        return e

if __name__ == '__main__':
    try:
        if type(validate(Exception)) is Exception:
            raise validate(Exception)
        p=4/0
        print "Buenos dias"
    except Exception as e:
        print e


    if kwargs is not None:
        for key, value in kwargs.iteritems():
            if key =="time":
                time=value
            elif key=="test":
                test=value
            else:
                test=False
                Value=True
