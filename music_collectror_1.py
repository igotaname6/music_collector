import csv
import sys
import os.path
import datetime
import random


def check_csv_existing():
    '''check if music.csv exist and create it if don't.'''
    if os.path.isfile("music.csv") is False:
        create_file = input("\nmusic.csv file does not exist. If you want to \
create it, enter Y.").upper()
        if create_file == "Y":
            os.mknod("music.csv")
        else:
            sys.exit("Bye, Bye!")


def read_csv():
    """Check if read csv is broken and save data to propper list"""
    with open('music.csv', 'r', encoding="utf-8-sig") as csv_file:  # save and read only utf8 chars
        reader = csv.reader(csv_file)
        music = []  # list with data read from csv file
        try:
            for line in reader:
                record = line[0].split("|")
                record_tuple = (record[0].strip(), record[1].strip()), \
                    (record[2].strip(), record[3].strip(), record[4].strip())
                # [0] = artist name, [1] = album title, [2] = relese year
                # [3] = genere, [4] = album lenght
                music.append(record_tuple)
        except IndexError:
            print("""music.csv file is broken. Reapir it manually or create a new one.
Make sure that every record is in one line, and each of five line elements
is separreted by '|'. Furthermore delete all blank lines""")
            quit_input = input("\nPress any key to quit\n")
            sys.exit("Bye, bye!")
    return music


def year_checkig(records_list):
    '''check if albums' releses years are propper integers > 1900'''
    year_check = True
    for record in records_list:
        try:
            int_from_year = int(record[1][0])
        except ValueError:
            print("\nData error: year is not propper integer. Please repair it manually\n")
            year_check = False
        if int(record[1][0]) < 1900:
            print("\nYear of relase can't be smaller than 1900. \
Please change it manually in csv file\n")
            year_check = False
    return year_check


def add_album():
    '''add album with informations to csv file'''
    artist = input("Enter an artist name: \n")
    album = input("Enter an album title: \n")
    year = input("Enter a year in which album was relesed: \n")
    while not year.isdigit():
        year = input("inappropriate date. Enter year again: \n")
    genere = input("Enter a genere of album: \n")
    lenght = input("Enter lenght of album(in format mm:ss): \n").split(":")
    with open('music.csv', 'a', encoding="utf-8-sig") as csv_file:
        writer = csv.writer(csv_file, delimiter="|")
        writer.writerow([artist, album, year, genere, lenght])


def find_album_by_artist(records_list):
    '''find album by artist name'''
    artist_name = input("\nEnter an artist name: \n")
    artist_found = False
    for record in records_list:
        if artist_name.upper() == record[0][0].upper():  # checking list form csv
            print(record[0][0], "-", record[0][1])
            artist_found = True
    if artist_found is False:
        press_key_to_continue = input("\nThere is no the artist's album in \
database. Press any key to continue.\n")
    else:
        press_key_to_continue = input("\nPress any key to contiune.\n")


def find_album_by_year(records_list):
    '''find album by year of relase'''
    year_of_relese = input("\nEnter year of album relese: \n")
    while not year_of_relese.isdigit():  # check if entered year is digit/
        year_of_relese = input("\nEnter a propper year: \n")
    year_found = False
    for record in records_list:
        if year_of_relese == record[1][0]:
            print(record[0][0], "-", record[0][1])  # print artist name and title
            year_found = True                       # from list
    if year_found is False:
        press_key_to_continue = input("\nThere is no album relesed in this year\
 in database. Press any key to continue.\n")
    else:
        press_key_to_continue = input("\nPress any key to contiune.\n")


def find_artist_by_album(records_list):
    '''find artist by entered album title'''
    album_name = input("\nEnter an album's title:\n")
    album_found = False
    for record in records_list:
        if album_name.upper() == record[0][1].upper():
            print(record[0][0])  # print artist name
            album_found = True
            break
    if album_found is False:
        press_key_to_continue = input("\nThere is no this title \
in database. Press any key to continue.\n")
    else:
        press_key_to_continue = input("\nPress any key to contiune.\n")


def find_album_by_letter(records_list):
    '''find album by letter or letters.'''
    letter_to_find = input("\nEnter a letter or letters to find in titles: \n")
    letter_found = False  # checking if variable is find in records_list
    for record in records_list:
        if letter_to_find.upper() in record[0][1].upper():
            print(record[0][0], "-", record[0][1])
            letter_found = True
    if letter_found is False:
        press_key_to_continue = input("\nThere is no title contains entered letters \
in database. Press any key to continue.\n")
    else:
        press_key_to_continue = input("\nPress any key to contiune.\n")


def find_album_by_genere(records_list):
    '''find albums by prompted genere'''
    entered_genere = input("\nEnter a genere to find: \n")
    genere_found = False
    for record in records_list:
        if entered_genere.upper() == record[1][1].upper():
            print(record[0][0], "-", record[0][1])
            genere_found = True
    if genere_found is False:
        press_key_to_continue = input("\nThere isn't the genere \
in database. Press any key to continue.\n")
    else:
        press_key_to_continue = input("\nPress any key to contiune.\n")


def calculate_age_of_albums(records_list):
    '''return sum of all albums ages'''
    current_year = datetime.datetime.now().year
    ages_sum = 0  # hold a sum of albums' ages
    for record in records_list:
        album_age = current_year - int(record[1][0])
        ages_sum += album_age
    return ages_sum


def random_album_by_genere(records_list):
    '''return random album by entered genere'''
    entered_genere = input("\nEnter a genere to find: \n")
    genere_found = False
    records_list_to_draw = []      # create list with all records by entered genere
    for record in records_list:
        if entered_genere.upper() == record[1][1].upper():  # check if entered genere
            records_list_to_draw.append(record[0])  # ... is in list and append record to drawing lis
            genere_found = True
    if genere_found is False:
        press_key_to_continue = input("\nThere isn't the genere \
in database. Press any key to continue.\n")
    else:
        random_album = random.choice(records_list_to_draw)
        print("Random album: ", random_album[0], "-", random_album[1])
        press_key_to_continue = input("\nPress any key to contiune.\n")


def show_amount_by_artist(records_list):
    '''show amount albums of entered artist'''
    entered_artist = input("\nEnter an artist name: \n")
    artist_found = False
    amount = 0
    for record in records_list:
        if entered_artist.upper() == record[0][0].upper():
            amount += 1
            artist_found = True
    if artist_found is False:
        press_key_to_continue = input("\nThere isn't the artist \
in database. Press any key to continue.\n")
    else:
        print("Total amount of", entered_artist, "albums:", amount)
        press_key_to_continue = input("\nPress any key to contiune.\n")


def menu():
    """menu with input from user"""
    option = input("""Choose the action:
     1) Add new album
     2) Find albums by artist
     3) Find albums by year
     4) Find musician by album
     5) Find albums by letter(s)
     6) Find albums by genre
     7) Calculate the age of all albums
     8) Choose a random album by genre
     9) Show the amount of albums by an artist
     0) Exit \n """)
    return option


def main():
    print("Welcome in the CoolMusic!")
    check_csv_existing()
    records_list = read_csv()

    while True:
        chosen_option = menu()

        if chosen_option == "1":
            add_album()
            records_list = read_csv()  # update records_list after adding new album

        elif chosen_option == "2":
            find_album_by_artist(records_list)

        elif chosen_option == "3":
            find_album_by_year(records_list)

        elif chosen_option == "4":
            find_artist_by_album(records_list)

        elif chosen_option == "5":
            find_album_by_letter(records_list)

        elif chosen_option == "6":
            find_album_by_genere(records_list)

        elif chosen_option == "7":
            year_check = year_checkig(records_list)  # check if it can sum years data
            if year_check is False:
                press_key_to_continue = input("\nPress any key to contiune.\n")
            else:
                print("\nSum of all albums ages = ", calculate_age_of_albums(records_list), "\n")
                press_key_to_continue = input("\nPress any key to contiune.\n")

        elif chosen_option == "8":
            random_album_by_genere(records_list)

        elif chosen_option == "9":
            show_amount_by_artist(records_list)

        elif chosen_option == "0":
            sys.exit("Bye, bye! ")

        else:
            print("\nChoose an option from list please. \n")


if __name__ == '__main__':
    main()
