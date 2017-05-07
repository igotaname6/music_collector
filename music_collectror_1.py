import csv
import sys


def read_from_csv():
    '''convert csv file to python list'''
    with open('music.csv', 'r', encoding="utf-8-sig") as csv_file:  # save and read only utf8 chars
        reader = csv.reader(csv_file)
        music = []  # list with data read from csv file
        for line in reader:
            record = line[0].split("|")
            record_tuple = (record[0].strip(), record[1].strip()), \
                (record[2].strip(), record[3].strip(), record[4].strip())
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



add_album() ssorsaw
