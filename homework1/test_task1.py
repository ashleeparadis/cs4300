import task1

#Pytest case to test output of task1
def test_hello_world(capfd):
    task1.hello_world()
    output = capfd.readouterr()
    assert output.out.strip() == "Hello, World!"
