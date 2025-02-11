import task7, requests

#Case to test if request to website is successful or has a status code of 200
def test_status_code_check():
    assert task7.check_status_code() == True

