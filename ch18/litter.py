import os


def get_dirlist(path):
    """
    Return a sorted list of all entries in path.
    This returns just the names, not full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def create_files(path, filename):
    """ Print recursive listing of contents of path """
    directory = os.path.join(path, filename)
    file = open(directory, "w")
    file.close()
    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)  # Turn name into full pathname
        if os.path.isdir(fullname):  # If director, recurse
            create_files(fullname, filename)


create_files("/Users/chasefrankenfeld/Documents/Test/", "trash.txt")
