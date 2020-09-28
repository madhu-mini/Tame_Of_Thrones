import abc


class Encryption(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_decrypted_msg(self, **kwargs):
        pass


class SeasarCipher(Encryption):

    def __init__(self):
        super(SeasarCipher, self).__init__()

    @staticmethod
    def get_decrypted_msg(**kwargs):
        """
        This function is used to return the decrypted message which is encrypted bu SeasarCipher technique.
        :param kwargs:
        :return: return the message in decrypted form
        """
        msg = kwargs['msg']
        key = kwargs['key']
        key = key % 26
        # Doing the reveres shift to get decrypted msg so if need to go 4 backwards going 22 place forward
        key = 26 - key
        decrypted_msg = ''
        for letter in msg:
            # uppercase characters
            if letter.isupper():
                decrypted_msg += chr((ord(letter) + key - 65) % 26 + 65)
            # lowercase characters
            else:
                decrypted_msg += chr((ord(letter) + key - 97) % 26 + 97)
        return decrypted_msg
