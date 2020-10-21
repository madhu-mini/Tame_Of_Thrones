from tame_of_thrones.constants import constant
from tame_of_thrones.exceptions.kingdom_exceptions import InvalidKingdomError


class Kingdom(object):

    def __init__(self, name, emblem, king_name=None):
        self.name = name
        self.emblem = emblem
        self.king_name = king_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is None or name is '':
            raise InvalidKingdomError("Kingdom name must not be empty.")
        if name.upper() not in constant.KINGDOMS_EMBLEM.keys():
            raise InvalidKingdomError("Kingdom with unknown emblem,Invalid Output.")
        self.__name = name

    @property
    def emblem(self):
        return self.__emblem

    @emblem.setter
    def emblem(self, emblem):
        if emblem is None or emblem is '':
            raise InvalidKingdomError("Kingdom emblem must not be empty.")
        if emblem.upper() not in constant.KINGDOMS_EMBLEM.values():
            raise InvalidKingdomError("Kingdom with invalid emblem.")
        self.__emblem = emblem

    @property
    def king_name(self):
        return self.__king_name

    @king_name.setter
    def king_name(self, king_name):
        self.__king_name = king_name

    def __repr__(self):
        return " Kingdom(Name : '{}', Emblem: '{}' , King = '{}' )".format(self.name, self.emblem, self.__king_name)

    def __str__(self):
        return " Kingdom : {} emblem : {} ".format(self.name, self.emblem)
