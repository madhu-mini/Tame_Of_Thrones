import sys

from Kingdom import Kingdom
from Universe import Universe
from War import War
from constant import KINGDOMS_EMBLEM


def main():
    # sys.argv[1] should give the absolute path to the input file
    input_file = sys.argv[1]
    # input_file = '/home/madhusudhan/PycharmProjects/Tame_Of_Thrones/input/input1.txt'

    # parse the file and process the command

    # creating southeros_universe and adding space kingdom
    southeros_universe = Universe('Southeros')
    space_kingdom = Kingdom('SPACE', 'Gorilla', 'King Shan')
    southeros_universe.addKingdom(space_kingdom)

    # reading the input from the file
    file1 = open(input_file, "r")
    input_text = file1.readlines()
    for kingdom_data in input_text:
        kingdom_name, sep, kingdom_msg = kingdom_data.partition(" ")
        new_kingdom = Kingdom(kingdom_name, KINGDOMS_EMBLEM[kingdom_name])
        # check whether space kingdom wins ove other kingdom if it is add to universe
        if War.result(new_kingdom, kingdom_msg):
            southeros_universe.addKingdom(new_kingdom)

    # print the output
    if southeros_universe.getNoOfKingdom() >= 4:
        print(southeros_universe.getKingdom())
    else:
        print("None")


if __name__ == "__main__":
    main()
