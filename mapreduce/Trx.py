__author__ = 'renatowalliser'

class Trx(object):

    def __init__(self):
        self.trxnum = None
        self.storename = None
        self.storeid = None
        self.type = None
        self.term = None

    def __str__(self):
        return ', '.join("%s:%s" % item for item in vars(self).items())
