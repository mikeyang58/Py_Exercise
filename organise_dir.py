#!/usr/bin/env python
"""
This script help you organization your dictory
Reference https://github.com/geekcomputers/Python/blob/master/Organise.py
"""
import os
import sys
import shutil

DEBUG = False 

Music = ['MP3', 'WAV', 'WMA', 'MKA', 'AAC', 'MID', 'RA', 'RAM', 'RM', 'OGG']
Codes = ['CPP', 'RB', 'PY', 'HTML', 'CSS', 'JS']
Compressed = ['RAR', 'JAR', 'ZIP', 'TAR', 'MAR', 'ISO', 'LZ', '7ZIP', 'TGZ', 'GZ', 'BZ2']
Documents = ['DOC', 'DOCX', 'PPT', 'PPTX', 'PAGES', 'PDF', 'ODT', 'ODP', 'XLSX', 'XLS', 'ODS', 'TXT', 'IN', 'OUT', 'MD']
Images = ['JPG', 'JPEG', 'GIF', 'PNG', 'SVG']
Executables = ['LIK', 'DEB', 'EXE', 'SH', 'BUNDLE']
Video = ['FLV', 'WMV', 'MOV', 'MP4', 'MPEG', '3GP', 'MKV', 'AVI']

def getVideo():
    return Video

def getMusic():
    return Music

def getCodes():
    return Codes

def getCompressed():
    return Compressed

def getImages():
    return Images

def getExe():
    return Executables

def getDoc():
    return Documents


try:
    arrange_dir = str(sys.argv[1])
except IndexError:
    arrange_dir = str(raw_input('Enter the path of dirctory:'))


def change(direc):
    try:
        os.chdir(direc)
    except OSError:
        print "Error! Cannot change the Directory"
        print "Enter a valid directory!"
        direc = str(raw_input("Enter the path of directory:"))
        change(direc)

change(arrange_dir)

list_dir = os.listdir(os.getcwd())

main_names = ['Video', 'Folders', 'Images', 'Documents', 'Music', 'Codes', 'Executables', 'Compressed']

def setDir(arr_dir,name,d_type):
    """
    Args:
        arr_dir: you want to settle dic
        name: a file or dic name
        d_type: a dictory's name
    Return:
        Null
    Example:
    setDir(arr_dir, name, 'dic_name')
    """
    try:
        os.mkdir(d_type)
        print d_type + "Folder Created"
    except OSError:
        print d_type + "Folder Exists"
    old_dir = arr_dir + "/" + name
    new_dir = arr_dir + "/" + d_type
    os.chdir(new_dir)
    shutil.move(old_dir, new_dir + "/" + name)
    print os.getcwd()
    os.chdir(arr_dir)

for name in list_dir:
    if len(name.split('.')) == 2:
        if name.split('.')[1].upper() in getVideo():
            setDir(arrange_dir, name, 'Video')

        elif name.split('.')[1].upper() in getImages():
            setDir(arrange_dir, name, 'Images')
        
        elif name.split('.')[1].upper() in getMusic():
            setDir(arrange_dir, name, 'Music')
        
        elif name.split('.')[1].upper() in getDoc():
            setDir(arrange_dir, name, 'Documents')

        elif name.split('.')[1].upper() in getCodes():
            setDir(arrange_dir, name, 'Codes')

        elif name.split('.')[1].upper() in getExe():
            setDir(arrange_dir, name, 'Exe')

        elif name.split('.')[1].upper() in getCompressed():
            setDir(arrange_dir, name, 'Compressed')

    else:
        if name not in main_names:
            setDir(arrange_dir, name, 'Folders')
