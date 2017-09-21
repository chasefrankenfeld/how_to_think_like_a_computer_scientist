import os


def get_dirlist(path):
    """
    Return a sorted list of all entries in path.
    This returns just the names, not full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_files(path, prefix=""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outerost call, path a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix + f)  # Print the line
        fullname = os.path.join(path, f)  # Turn name into full pathname
        if os.path.isdir(fullname):  # If director, recurse
            print_files(fullname, prefix + "| ")


# print_files("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pygame/examples/")

file_list = []


def print_full_path(path, prefix=True):
    """ Return a list of all the full paths of files in a directory or subdirectory of a path """
    if prefix:  # Detect outer most call, path a heading
        print("Full paths of files in the directory or subdirectory", path, "include:")

    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            print_full_path(fullname, prefix=False)
        elif os.path.isfile(fullname):
            file_list.append(fullname)
    return file_list


print_full_path("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pygame/examples/")

for i in file_list:
    print(i)
