import task6, pytest

#Function to dynamically generate function names base on filename
def create_test(filename, word_count):
    def test_count_words():
        assert task6.count_words(filename) == word_count   #Check word count of file

    #Create function name based on file name
    test_count_words.__name__ = f"test_{filename.replace(".", "_")}_count_words"
    return test_count_words

#Create new test case for task6 read me
test_file_1 = create_test("task6_read_me.txt", 127)

globals()[test_file_1.__name__] = test_file_1


