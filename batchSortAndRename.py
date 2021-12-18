#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def main(directory):
    allFiles = os.listdir(directory)
    if len(allFiles) > 0:
        try:
            allFiles.sort(key=lambda x: x.split('_')[1])
        except:
            print('Timestamp not found')

        for file in allFiles:
            fileExtension = file.split('.')[-1]
            newFileName = directory + \
                str(allFiles.index(file)) + '.' + fileExtension
            try:
                os.rename(directory + file, newFileName)
            except:
                print('Old file not found')


if __name__ == '__main__':
    directory = os.path.join(BASE_PATH, 'images', '')
    if len(sys.argv) is 2:
        directory = os.path.join(BASE_PATH, sys.argv[1], '')
    if os.path.exists(directory):
        main(directory)
    else:
        print('Please specify a directory')
