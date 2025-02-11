import task6, os, pytest

text_files_path = os.getcwd()    #Get path of current working directory

#Get list of all text files in cwd
text_files = [i for i in os.listdir(text_files_path) if i.endswith(".txt")]

#Dynamically define test cases with a decorator
@pytest.mark.parametrize("name, words", [("task6_read_me.txt", 127)])
def test_file_word_count(name, words):
    path = os.path.join(text_files_path, name)

    assert task6.count_words(path) == words


