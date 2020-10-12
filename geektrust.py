import sys

from tame_of_thrones.kingdom import Kingdom
from tame_of_thrones.universe import Universe
from tame_of_thrones.war import War
from tame_of_thrones.constants.constant import KINGDOMS_EMBLEM, MIN_NO_OF_WINS


def main():
    # input_file = sys.argv[1]
    input_file = '/home/madhusudhan/PycharmProjects/Tame_Of_Thrones/input/input1.txt'

    # creating southeros_universe and adding space kingdom
    southeros_universe = Universe('Southeros')
    space_kingdom = Kingdom('SPACE', 'Gorilla', 'King Shan')
    southeros_universe.add_kingdom(space_kingdom)

    # parse the file and process the command
    input_reader = open(input_file, "r")
    input_text = input_reader.readlines()
    for kingdom_data in input_text:
        kingdom_name, separator, kingdom_message = kingdom_data.partition(" ")
        new_kingdom = Kingdom(kingdom_name, KINGDOMS_EMBLEM[kingdom_name])
        if War.get_war_result(new_kingdom, kingdom_message):
            southeros_universe.add_kingdom(new_kingdom)

    # print the output
    if southeros_universe.get_no_of_kingdom() > MIN_NO_OF_WINS:
        print(southeros_universe.get_kingdom())
    else:
        print("None")


if __name__ == "__main__":
    main()
