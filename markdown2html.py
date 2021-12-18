#!/usr/bin/python3
'''
Markdown to HTML
'''
from sys import argv
from sys import stderr
from os.path import exists

def main():
    n_args = len(argv)
    if n_args < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    input_file_name = argv[1]
    output_file_name = argv[2]
    if not exists(input_file_name):
        print("Missing " + input_file_name, file=stderr)
        exit(1)
    exit(0)

if __name__ == "__main__":
    main()
