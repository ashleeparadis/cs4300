import task4

#Pytest case to test the input calculate_discount() can handle
def test_calculate_discount():
    assert task4.calculate_discount(70, 10) == 63
    assert task4.calculate_discount(95.5,  12.5) == 83.5625
    assert task4.calculate_discount(100,  15.5) == 84.5