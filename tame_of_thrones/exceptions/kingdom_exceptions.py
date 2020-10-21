class InvalidKingdomError(Exception):
    def __init__(self, msg=''):
        self.msg = "Invalid Kingdom: " + msg

    def __str__(self):
        return repr(self.msg)