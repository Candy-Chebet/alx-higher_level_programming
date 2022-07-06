#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8) and returns the number of characters written
"""
def write_file(filename="", text=""):

            if filename =="" or type(filename) ! = str:
            return 0

        count = 0
        with open(UTF8, 'w' encoding="utf-8") as f:
            for line in f:
                count += 1
        return count
