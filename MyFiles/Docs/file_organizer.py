"""
Create a new Python script named file_organizer.py.
Use the os.mkdir() function to create a new directory named MyFiles.
Inside MyFiles, create three subdirectories named Docs, Images, and Videos using the same mkdir() function.
    """

import os


def main():
    os.mkdir("MyFiles")
    os.mkdir("MyFiles/Docs")
    os.mkdir("MyFiles/Images")
    os.mkdir("MyFiles/Videos")


main()
