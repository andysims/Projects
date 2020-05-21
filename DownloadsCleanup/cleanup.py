"""
Downloads Cleanup
This script runs through Downloads folder
It reads the extension of the file (ex: .pdf)
It takes extension and creates a folder (if doesn't exist)
Puts files in correct folder
"""
import os
import shutil
# import getpass

# user = getpass.getuser()
home_dir = os.path.expanduser("~")
downloads = home_dir + "/Downloads"
trash = home_dir + "/.Trash"
files_in_downloads = os.listdir(downloads)
ignore_files = [".DS_Store", ".localized"]
shapefile = ['shp', 'shx', 'dbf', 'prj', 'xml', 'sbn', 'sbx', 'cpg', 'qix']


def get_extensions(file_list):
    temp_list = []
    for file in file_list:
        if file not in ignore_files:
            ext = os.path.splitext(file)
            ext = ext[1].replace(".", "")
            temp_list.append(ext)
    extensions = set(temp_list[:])
    return extensions


def create_dirs():
    create_ext = get_extensions(files_in_downloads)
    for extension in create_ext:
        dir_ext = downloads + "/" + extension
        if not os.path.isdir(dir_ext):
            os.mkdir(dir_ext)


def move_files():
    create_dirs()
    for file in files_in_downloads:
        if file not in ignore_files:
            try:
                f = os.path.splitext(file)[1].replace(".", "")
                file_loc = f"{downloads}/{file}"
                mv_loc = f"{downloads}/{f}/{file}"
                shutil.move(file_loc, mv_loc)
            except FileNotFoundError:
                print(f"File not found: {file}")


def del_dir():
    for file in files_in_downloads:
        if file not in ignore_files:
            path = f"{downloads}/{file}"
            length = len(os.listdir(path))
            if length == 0:
                shutil.move(path, trash)


move_files()
del_dir()
