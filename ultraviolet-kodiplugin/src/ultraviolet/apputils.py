__author__ = 'developer'


def cleanString( str):
    if not str is None:
        return str.replace("'", "")

def cleanStringOs(str):
    if not str is None:
        return str.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)").replace("'", "")

def getInput(msg, length):
    res = input(msg)
    if (res==None or (res!=None  and res=="" )):
        if (length>0):
            res = 0
    return res


