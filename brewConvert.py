import mmap

brewFile = ("BrewTest.rb")


def check_If_Brew_File():
    with open('BrewTest.rb') as file, \
            mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if s.find(b'class') != -1:  # TODO: Perhaps improve the checks ?
            return True
        else:
            return False


def get_url():
    file_as_string = open('BrewTest.rb')
    enumated_lines = file_as_string.readlines()
    url_static = str(enumated_lines[3])
    if "url" in url_static:
        print("I think this works :)")
        print("Test of replacing the string")

        delete_url = str(url_static.replace("url", ""))
        delete_comas = str(delete_url.replace('"', ""))
        final_url = delete_comas.strip()
        print(final_url)
        return final_url
       # else:
        #print("Nope lol")
