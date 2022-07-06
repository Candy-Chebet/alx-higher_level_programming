#!/usr/bin/python3
''' function that returns the number of lines of a text file'''
def write_file(filename="", text=""):

            if filename =="" or type(filename) ! = str:
            return 0

        count = 0
        with open(UTF8.txt, 'w' encoding="utf-8") as f:
            for line in f:
                count += 1
        return count
