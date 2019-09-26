from brewConvert import check_If_Brew_File, get_url
from brewDownloader import download_files
import os
import sys

brewConvertPath = "brewConvert.py"
sys.path.append(os.path.abspath(brewConvertPath))


def main():
    print("Checking if it is a valid brew file")
    if check_If_Brew_File() == True:
        print("It was true bruh")
    else:
        print("It was fake bruh")
        exit()


main()
get_url()
download_files()
