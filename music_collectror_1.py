import csv
import sys
import os.path


def check_csv_existing():
    '''check if music.csv exist and create it if don't.'''
    if os.path.isfile("music.csv") is False:
        create_file = input("\nmusic.csv file does not exist. If you want to \
create it, enter Y.").upper()
        if create_file == "Y":
            os.mknod("music.csv")
        else:
            print("Bye, Bye")
            sys.exit()


def read_csv():
    """Read csv file and save data to propper list"""
    with open('music.csv', 'r', encoding="utf-8-sig") as csv_file:  # save and read only utf8 chars
        reader = csv.reader(csv_file)
        music = []  # list with data read from csv file
        for line in reader:
            record = line[0].split("|")
            record_tuple = (record[0].strip(), record[1].strip()), \
                (record[2].strip(), record[3].strip(), record[4].strip())
            # [0] = artist name, [1] = album title, [2] = relese year
            # [3] = genere, [4] = album lenght
            music.append(record_tuple)
    return music


def add_album():
    '''add album with informations to csv file'''
    artist = input("Enter an artist name: \n")
    album = input("Enter an album title: \n")
    year = input("Enter a year in which album was relesed: \n")
    genere = input("Enter a genere of album: \n")
    lenght = input("Enter lenght of album: \n")
    with open('music.csv', 'a', encoding="utf-8-sig") as csv_file:
        writer = csv.writer(csv_file, delimiter="|")
        writer.writerow([artist, album, year, genere, lenght])


def menu():
    """menu with input from user"""
    option = input(""" Welcome in the CoolMusic! Choose the action:
     1) Add new album
     2) Find albums by artist
     3) Find albums by year
     4) Find musician by album
     5) Find albums by letter(s)
     6) Find albums by genre
     7) Calculate the age of all albums
     8) Choose a random album by genre
     9) Show the amount of albums by an artist *
     10) Find the longest-time album *
     0) Exit \n """)
    return option


def main():
    check_csv_existing()
    records_list = read_csv()

    while True:
        chosen_option = menu()
        if chosen_option == "1":
            add_album()
            records_list = read_csv() #update records_list after adding new album
        elif chosen_option == "0":
            sys.exit("Bye, bye! ")
        else:
            print("\nChoose an option please. \n")



if __name__ == '__main__':
    main()
