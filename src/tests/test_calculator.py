"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition():
    calc = Calculator()
    assert calc.addition(2, 3) == 5

def test_addition_failing():
    calc = Calculator()
    assert calc.addition(2, 2) == 4 #changed from 5 to 4
