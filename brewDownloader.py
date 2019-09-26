from brewConvert import get_url
import wget


def download_files():
    wget.download(get_url(), '/Volumes/DiegoDrive/Projects/Code/Brew2Sput')
