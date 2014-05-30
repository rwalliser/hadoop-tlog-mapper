__author__ = 'renatowalliser'

class Trx(object):

    def __init__(self):
        self.training = None
        self.date = None
        self.terminaltype = None
        self.ringtime = None
        self.type = None
        self.realdate = None
        self.total = None
        self.retailtotal = None
        self.endtime = None
        self.retrieved = None
        self.storename = None
        self.trxnum = None
        self.tndtime = None
        self.opername = None
        self.term = None
        self.storeid = None
        self.opcode = None
        pass
    
    def getAttribute(self):
        return ','.join("%s" % item[0] for item in vars(self).items())
    
    def __str__(self):
        result = ','.join("%s" % item[1] for item in vars(self).items()) 
        return  result.encode('utf-8')
#         return ', '.join("%s:%s" % item for item in vars(self).items())
