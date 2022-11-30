from app.calculator import Calculator
import pytest


class Test_calculator:
    def setup(self):
        self.calc = Calculator

    def test_multiple_calculate_correct(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiple_calculate_filed(self):
        assert self.calc.multiply(self, 2, 3) == 7
