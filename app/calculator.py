class Calculator:
    def multiply(self, x, y):
        return x * y

    def division(self, x, y):
        return x - y

    def subtraction(self, x, y):
        return x - y

    def adding(self, x, y):
        return x + y


def multiply(x, y):
    return x * y

def test_multiply():
    assert multiply(2, 2) == 5