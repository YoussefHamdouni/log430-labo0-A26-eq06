"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# ---------- Message de bienvenue ----------

def test_app(calc):
    welcome_message = calc.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message


def test_hello_message_with_env(calc, tmp_path, monkeypatch):
    (tmp_path / ".env").write_text("CALCULATOR_USERNAME=Equipe06")
    monkeypatch.chdir(tmp_path)
    assert "Bienvenu(e) Equipe06" in calc.get_hello_message()


def test_hello_message_without_env(calc, tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)  # dossier vide : aucun .env
    message = calc.get_hello_message()
    assert message == "== Calculatrice v1.0 ==\n"
    assert ".env n'était pas trouvé" in capsys.readouterr().out


# ---------- Addition ----------

def test_addition(calc):
    assert calc.addition(2, 3) == 5


def test_addition_failing(calc):
    # Test volontairement en échec pour la question 1 (2 + 2 == 5), corrigé ensuite
    assert calc.addition(2, 2) == 4


@pytest.mark.parametrize("v1, v2, expected", [
    (0, 0, 0),
    (-2, -3, -5),
    (-2, 5, 3),
    (10**12, 10**12, 2 * 10**12),
])
def test_addition_edge_cases(calc, v1, v2, expected):
    assert calc.addition(v1, v2) == expected


def test_addition_floats(calc):
    assert calc.addition(0.1, 0.2) == pytest.approx(0.3)


# ---------- Soustraction ----------

def test_subtraction(calc):
    assert calc.subtraction(10, 4) == 6


@pytest.mark.parametrize("v1, v2, expected", [
    (0, 0, 0),
    (3, 5, -2),
    (-3, -5, 2),
    (5, 0, 5),
])
def test_subtraction_edge_cases(calc, v1, v2, expected):
    assert calc.subtraction(v1, v2) == expected


# ---------- Multiplication ----------

def test_multiplication(calc):
    assert calc.multiplication(3, 4) == 12


@pytest.mark.parametrize("v1, v2, expected", [
    (5, 0, 0),
    (0, 0, 0),
    (-3, 4, -12),
    (-3, -4, 12),
    (1, 7, 7),
])
def test_multiplication_edge_cases(calc, v1, v2, expected):
    assert calc.multiplication(v1, v2) == expected


def test_multiplication_floats(calc):
    assert calc.multiplication(2.5, 0.4) == pytest.approx(1.0)


# ---------- Division ----------

def test_division(calc):
    assert calc.division(10, 2) == 5


def test_division_non_integer_result(calc):
    assert calc.division(7, 2) == 3.5
    assert calc.division(1, 3) == pytest.approx(0.3333, rel=1e-3)


@pytest.mark.parametrize("v1, v2, expected", [
    (0, 5, 0),
    (-10, 2, -5),
    (-10, -2, 5),
])
def test_division_edge_cases(calc, v1, v2, expected):
    assert calc.division(v1, v2) == expected


def test_division_by_zero(calc):
    assert calc.division(5, 0) == "Erreur : division par zéro"
    assert calc.last_result == "Error"


def test_division_zero_by_zero(calc):
    assert calc.division(0, 0) == "Erreur : division par zéro"


# ---------- État interne ----------

def test_last_result_initial_value(calc):
    assert calc.last_result == 0


def test_last_result_updated_after_each_operation(calc):
    calc.addition(1, 1)
    assert calc.last_result == 2
    calc.subtraction(5, 3)
    assert calc.last_result == 2
    calc.multiplication(3, 3)
    assert calc.last_result == 9
    calc.division(9, 3)
    assert calc.last_result == 3
