from os import listdir, path


def print_directory_contents(sPath):
    if path.isfile(sPath):
        print(sPath)
        return

    for directory in listdir(sPath):
        new_path = path.join(sPath, directory)
        print_directory_contents(new_path)
