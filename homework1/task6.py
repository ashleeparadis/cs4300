import os

path = os.path.join(os.getcwd(), "task6_read_me.txt")

#Function that reads a file and returns the number of words in it

def count_words(filepath):
    file = open(filepath, "r")         #Open file for reading
    words = file.read()
    word_count = len(words.split())    #Split string into list of words using spaces
    return word_count
    file.close()

count_words(path)
