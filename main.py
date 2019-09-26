from brewconverter import check_if_brew_file, get_url
from brewdownloader import download_files
import os
import sys


def main():
    print("Checking if it is a valid brew file")
    if check_if_brew_file == True:
        print("It was true bruh")
    else:
        print("It was fake bruh")
        exit()


main()
get_url()
download_files()
