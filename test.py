import nltk

file_path = "Documents/text.txt"

with open(file_path, "r") as file:
    file_contents = file.read()

tokens = nltk.word_tokenize(file_contents)