import task3

#Test the control structure that determines whether a number is negative or positive
def test_num_pos_neg():
    assert task3.check_pos_neg(-2) == "Number is negative"
    assert task3.check_pos_neg(4) == "Number is positive"

#Test control structure that calculates first 10 prime numbers
def test_first_10_primes():
    assert task3.get_first_10_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#Test control structure that calculates the sum of numbers between 1 and 100
def test_sum_numbers():
    assert task3.sum_numbers() == 5050
