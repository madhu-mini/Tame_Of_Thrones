class InvalidUniverseException(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class InvalidKingdomException(Exception):
    def __init__(self, msg=''):
        self.msg = "Invalid Kingdom: " + msg

    def __str__(self):
        return repr(self.msg)