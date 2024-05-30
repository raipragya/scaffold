from hello import add


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x


def test_hello_add():
    assert add(test_hello_add.x) == 11
