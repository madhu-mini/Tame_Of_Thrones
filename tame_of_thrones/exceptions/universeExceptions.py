class InvalidUniverseError(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class InvalidKingdomError(Exception):
    def __init__(self, msg=''):
        self.msg = "Invalid Kingdom: " + msg

    def __str__(self):
        return repr(self.msg)
