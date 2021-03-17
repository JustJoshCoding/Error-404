import os
import os.path
import sys
import io
import zipfile
import shutil
from pathlib import Path


def extract(filename):
    address = ''
    z = zipfile.ZipFile(filename)
    address2 = ''
    address3 = ''
    destination = ''

    for f in z.namelist():
        # get directory name from file
        dirname = os.path.splitext(f)[0]
        # create new directory
        os.mkdir(dirname)
        # read inner zip file into bytes buffer
        content = io.BytesIO(z.read(f))
        zip_file = zipfile.ZipFile(content)

        file_path = ''  # remembers entire file address of last file found per iteration
        filename = ''  # remembers name of last file found per iteration
        cwd = os.getcwd()
        dir = os.path.join("C:\\", cwd, "Programs")  # creates new folder
        if not os.path.exists(dir):  # makes sure that the folder is not made multiple times
            os.mkdir(dir)
        for file in zip_file.namelist():  # this iterates every directory found in the namelist buffer

            for root, subdirs, files in os.walk(dirname):  # this is how os.walk is used.
                name = ''
                for files in file:  # for some reason the files are found in characters so this loop iterates the name of the files found and updates the name sring variabe
                    name += files
                    file_path = os.path.join(root, name)
                    #print(root)
                    #print(file_path)
                    filename = name

            zip_file.extract(file, dirname)
            # this code was suppose to move the directory of the files found to the new folder created
            # os.rename(os.path.abspath(name), os.path.join(dir, name))

        #address = os.path.abspath(filename)
        address = os.getcwd() + '/' + root + '/' + os.path.normpath(filename)
        print(os.getcwd())
        #address = Path(filename).absolute()
        #raw_string = r"{}".format(address)
        #print(type(address))
        address3 = (r"C:\\Users\\shani\\PycharmProjects\\pythonProject\\077786745\\077786745\\Assignment1\\J.Obrien\\816001354")
        address = address.replace('\\', '/')
        #print(address2)
        print(
            'walk_dir (absolute) = ' + address)  # just a test print statement showing file addresses
        print('--------------------------------')

        # Move files
        destination = (r"C:/Users/shani/PycharmProjects/pythonProject/Programs")
        shutil.move(address, destination)
        #Path(address).rename(destination)

    # run the function here


extract('5678.zip')
