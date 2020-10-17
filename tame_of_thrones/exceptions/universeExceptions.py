class InvalidUniverseError(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class InvalidKingdomError(Exception):        #file name is univerExceptions. Either rename the file Name to something generic or create seperate classes. Also is the file name is according to conventions?
    def __init__(self, msg=''):
        self.msg = "Invalid Kingdom: " + msg

    def __str__(self):
        return repr(self.msg)
