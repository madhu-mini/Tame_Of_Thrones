import collections

from Encryption import SeasarCipher


class War:

    @staticmethod
    def getMapping(mapping_string):
        """
        This method is used to get the mapping of letters in input string
        :param mapping_string:
        :return: default_dictionary
        """
        key_map = collections.defaultdict(int)
        mapping_string = mapping_string.lower()
        for letter in mapping_string:
            if letter.isalpha():
                key_map[letter] += 1
        return key_map

    @staticmethod
    def result(kingdom, msg):
        """
        This method is used to get the war result if kingdom is attacked with specific msg
        :param kingdom:
        :param msg:
        :return: the result of war if kingdom is attacked with specific msg
        """
        key = len(kingdom.emblem)
        decrypted_msg = SeasarCipher.get_decrypted_msg(key=key, msg=msg)
        decrypted_msg_map = War.getMapping(decrypted_msg)
        key_map = War.getMapping(kingdom.emblem)
        for key in key_map.keys():
            if key_map[key] > decrypted_msg_map[key]:
                return False
        return True
