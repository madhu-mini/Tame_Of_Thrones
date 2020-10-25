import unittest
from unittest import TestCase

from tame_of_thrones.encryption import SeasarCipher


class TestSeasarCipher(TestCase):
    def test_get_decrypted_msg(self):
        self.assertEqual('olwl', SeasarCipher.get_decrypted_msg(message='rozo', decryption_key=3))

    def test_get_decrypted_msg_upper_case(self):
        self.assertEqual('OLWL', SeasarCipher.get_decrypted_msg(message='ROZO', decryption_key=3))

    def test_get_decrypted_msg_mixed_case(self):
        self.assertEqual('OlwL', SeasarCipher.get_decrypted_msg(message='RozO', decryption_key=3))

    def test_get_decrypted_msg_key(self):
        self.assertEqual('OlwL', SeasarCipher.get_decrypted_msg(message='RozO', decryption_key=3))

    def test_get_decrypted_msg_large_key(self):
        self.assertEqual('Live', SeasarCipher.get_decrypted_msg(message='Live', decryption_key=26))

    def test_get_decrypted_msg_zero_key(self):
        self.assertEqual('Live', SeasarCipher.get_decrypted_msg(message='Live', decryption_key=0))


if __name__ == '__main__':
    unittest.main()
