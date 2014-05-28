#!/usr/bin/python
__author__ = 'renatowalliser'

import sys
import cStringIO
import xml.etree.ElementTree as xml
import re
from Trx import Trx


def extraktTrxFromXml(value):
    root = xml.fromstring(value)
    trx = Trx()
    for attribute in vars(trx).items():
        trx.__setattr__(attribute[0], root.get(attribute[0]))
    return trx

if __name__ == '__main__':
    inTrx = None
    for line in sys.stdin:
        line = line.strip()

        if line.find("<TRX") != -1:
            
            outterXml = re.findall('(<TRX.*/>$)', line)
            if (len(outterXml)>0):
                print extraktTrxFromXml(outterXml[0])
                pass
            else:    
                inTrx = True
                xmlBuffer = cStringIO.StringIO()  # @UndefinedVariable
                xmlBuffer.write(line)
                pass
        elif line.find("</TRX>") != -1:
            inTrx = False
            xmlBuffer.write(line)
            value = xmlBuffer.getvalue()
            xmlBuffer.close()
            xmlBuffer = None
            print extraktTrxFromXml(value)
            pass
        else:
            if inTrx:
                xmlBuffer.write(line)
                pass
