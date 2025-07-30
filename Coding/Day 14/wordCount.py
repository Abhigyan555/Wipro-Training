'''
Name: Abhigyan Maji
ID: 30382
Date: 22 July 2025
Purpose: Count number of lines, words, and characters in a text file using command-line arguments.
'''

import argparse

def countLines(filename):
    with open(filename, 'r') as f:
        return len(f.readlines())

def countWords(filename):
    with open(filename, 'r') as f:
        return len(f.read().split())

def countCharacters(filename):
    with open(filename, 'r') as f:
        return len(f.read())

def main():
    parser = argparse.ArgumentParser(description="Count lines, words, and characters in a file.")
    parser.add_argument("filename", help="File to process")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
    parser.add_argument("-w", "--word", action="store_true", help="Count words")
    parser.add_argument("-c", "--char", action="store_true", help="Count characters")

    args = parser.parse_args()
    filename = args.filename

    output = []

    if args.lines:
        output.append(str(countLines(filename)))
    if args.word:
        output.append(str(countWords(filename)))
    if args.char:
        output.append(str(countCharacters(filename)))

    if not (args.lines or args.word or args.char):
        output = [str(countLines(filename)), str(countWords(filename)), str(countCharacters(filename))]

    output.append(filename)
    print('\t'.join(output))

if __name__ == "__main__":
    main()
