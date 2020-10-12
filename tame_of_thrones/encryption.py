import abc


class Encryption(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_decrypted_msg(self, message, decryption_key):
        pass


class SeasarCipher(Encryption):

    def __init__(self):
        super(SeasarCipher, self).__init__()

    @staticmethod
    def get_decrypted_msg(message, decryption_key):
        """
        This function is used to return the decrypted message which is encrypted bu SeasarCipher technique.
        :param message:
        :param decryption_key:
        :return:
        """
        decryption_key = decryption_key % 26
        decryption_key = 26 - decryption_key
        decrypted_msg = ''
        for letter in message:
            # uppercase characters
            if letter.isupper():
                decrypted_msg += chr((ord(letter) + decryption_key - 65) % 26 + 65)
            # lowercase characters
            else:
                decrypted_msg += chr((ord(letter) + decryption_key - 97) % 26 + 97)
        return decrypted_msg
