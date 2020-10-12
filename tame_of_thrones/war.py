import collections

from tame_of_thrones.encryption import SeasarCipher


class War:

    @staticmethod
    def get_string_mapping(mapping_string):
        """
        This method is used to get the mapping of letters in input string
        :param mapping_string:
        :return: default_dictionary
        """
        string_map = collections.defaultdict(int)
        mapping_string = mapping_string.lower()
        for letter in mapping_string:
            if letter.isalpha():
                string_map[letter] += 1
        return string_map

    @staticmethod
    def get_war_result(kingdom, message):
        """
        This method is used to get the war result if kingdom is attacked with specific msg
        :param kingdom:
        :param message:
        :return: the result of war if kingdom is attacked with specific msg
        """
        decryption_key = len(kingdom.emblem)
        decrypted_msg = SeasarCipher.get_decrypted_msg(message=message, decryption_key=decryption_key)
        decrypted_msg_map = War.get_string_mapping(decrypted_msg)
        emblem_map = War.get_string_mapping(kingdom.emblem)
        for letter in emblem_map.keys():
            if emblem_map[letter] > decrypted_msg_map[letter]:
                return False
        return True
