'''
Name: Abhigyan Maji
ID: 30382
Date: 22 July 2025
Purpose: Functional test for wordCount using capsys
'''

import wordCount
import sys

def test_all_counts(tmp_path, capsys):
    file = tmp_path / "sample.txt"
    file.write_text("Line one\nLine two\nLine three")
    sys.argv = ['wordCount.py', str(file)]
    wordCount.main()
    out = capsys.readouterr().out.strip().split()
    assert out[-1] == str(file.name)
    assert out[0] == "3"
    assert out[1] == "6"
    assert out[2].isdigit()

def test_line_flag(tmp_path, capsys):
    file = tmp_path / "lines.txt"
    file.write_text("One\nTwo\nThree")
    sys.argv = ['wordCount.py', '-l', str(file)]
    wordCount.main()
    out = capsys.readouterr().out.strip().split()
    assert out[0] == "3"
    assert out[1] == str(file.name)
