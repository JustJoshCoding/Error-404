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
    
    cwd = os.getcwd()
    dir = os.path.join("C:\\", cwd, "Programs")  # creates new folder
    if not os.path.exists(dir):  # makes sure that the folder is not made multiple times
        os.mkdir(dir)
    destination = dir
    for f in z.namelist():
        # get directory name from file
        dirname = os.path.splitext(f)[0]
        # create new directory
        os.mkdir(dirname)
        # read inner zip file into bytes buffer
        content = io.BytesIO(z.read(f))
        zip_file = zipfile.ZipFile(content)
        file_path = ''  # remembers entire file address of last file found per iteration
        for file in zip_file.namelist():  # this iterates every directory found in the namelist buffer
            for root, subdirs, files in os.walk(dirname):  # this is how os.walk is used.
                file_path = root
            zip_file.extract(file, dirname)
        address = cwd + '/' + file_path
        address = address.replace('\\', '/')
        try: 
            shutil.move(address, destination) 
            print("File moved successfully.") 
        # If source and destination are same 
        except shutil.SameFileError: 
            print("Source and destination represents the same file.") 
        # If there is any permission issue 
        except PermissionError: 
            print("Permission to move the files have been denied.")  
        # If the file already exist 
        except  FileExistsError:
            print("File Already Exist.")
        # If file was not found 
        except FileNotFoundError:
            print("Error: File Not Found.")
        # For other errors 
        except: 
            print("Error occurred while moving file.") 
        delfile = cwd + '/' + dirname
        delfile = delfile.replace('\\', '/')
        try: 
            shutil.rmtree(delfile)
            print("Successfully removed unwanted files.") 
        # If there is any permission issue 
        except PermissionError: 
            print("Permission to delete unwanted files denied.") 
        # If file was not found 
        except FileNotFoundError:
            print("Error: File Not Found.")
        # For other errors 
        except: 
            print("Error occurred while deleting file.")
        

# run the function here
extract('1234.zip')
