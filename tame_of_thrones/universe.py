import collections

from tame_of_thrones.constants import constant
from tame_of_thrones.exceptions.universe_exceptions import InvalidUniverseError


class Universe:

    def __init__(self, reigns, kingdoms=None):
        self.reigns = reigns
        self.kingdoms = kingdoms

    @property
    def reigns(self):
        return self.__reigns

    @reigns.setter
    def reigns(self, reigns):
        if reigns is None or reigns.upper() not in constant.UNIVERSE or reigns in '':
            raise InvalidUniverseError("Invalid Universe.")
        self.__reigns = reigns

    @property
    def kingdoms(self):
        return self.__kingdoms

    @kingdoms.setter
    def kingdoms(self, kingdoms):
        if kingdoms is None:
            self.__kingdoms = collections.OrderedDict()
        else:
            self.__kingdoms = kingdoms

    def __repr__(self):
        return " reigns : {} , kingdoms :  {} ".format(self.__reigns, self.__kingdoms)

    def __str__(self):
        return " reigns : {} , kingdoms :  {} ".format(self.__reigns, self.__kingdoms)

    def add_kingdom(self, kingdom):
        """
        This method is used to add kingdom to particular universe reigns.
        :param kingdom:
        :return:
        """
        if kingdom.name.upper() not in self.__kingdoms.keys():
            self.__kingdoms[kingdom.name.upper()] = kingdom

    def remove_kingdom(self, kingdom):
        """
        This method is used to remove kingdom from particular universe reigns.
        :param kingdom:
        :return:
        """
        if kingdom.name.upper() in self.__kingdoms.keys():
            del self.__kingdoms[kingdom.name]

    def get_kingdom(self):
        """
        It is used to get the all kingdoms belonging to particular universe.
        :return:
        """
        kingdom_str = ''
        for kingdom in self.__kingdoms:
            kingdom_str = kingdom_str + kingdom + ' '
        return kingdom_str

    def get_no_of_kingdom(self):
        return len(self.__kingdoms)
