from demo_python_app.main import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(8, 3) == 5
