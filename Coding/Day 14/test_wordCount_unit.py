'''
Name: Abhigyan Maji
ID: 30382
Date: 22 July 2025
Purpose: Unit tests for wordCount functions
'''

import wordCount

def test_count_lines(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello\nWorld\nThis\nis\npytest\n")
    assert wordCount.countLines(file) == 5

def test_count_words(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello World\nThis is pytest")
    assert wordCount.countWords(file) == 5

def test_count_characters(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("abc def")
    assert wordCount.countCharacters(file) == 7
