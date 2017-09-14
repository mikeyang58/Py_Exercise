#!/usr/bin/env python

from organise_dir import getVideo, getMusic, getDoc, getCodes, getExe, getCompressed,\
        getImages, change, setDir


f_list = [getMusic, getVideo, getDoc, getCodes, getExe, getCompressed]
arr_list = ['/Users/jiayuany', '/Users/jiayuany/Documents']

name_list = ['test1.jpg', 'test2.png', 'test3.xlsx', 'test4.doc', 'test5.py', 'test6.gz', 'test7.mp3']

type_list = ['Music', 'Video', 'Doc', 'Codes', 'Exe', 'Compressed']

setDir_list = [
        ('/Users/jiayuany/Documents', 'test1.jpg', 'Images'), 
        ('/Users/jiayuany', 'test2.doc', 'Doc'),
        ('/Users/jiayuany/Documents', 'test5.py', 'Codes'),
        ]

def test_get():
    for f in f_list:
        print f()
                    
def test_change():
    for d in arr_list:
        change(d)

def test_setDir():
    for s in setDir_list:
        arr_dir, name, d_type = s
        setDir(arr_dir, name, d_type)

test_setDir()
test_change()
test_get()
