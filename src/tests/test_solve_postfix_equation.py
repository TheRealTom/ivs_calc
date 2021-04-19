"""@package tests
Test for solving the postfix equation
"""

from duck_calc.math_lib.math_lib import MathLib
import pytest


@pytest.mark.parametrize("problem, result", [
    ("1 1 +", 2),
    ("11 9 +", 20),
    ("583 12 +", 595),
    ("-1 1 +", 0),
    ("-126 26 +", -100),
    ("987654321 123456789 +", 1111111110),
    ("-987654321 123456789 +", -864197532),

    ("1 1 -", 0),
    ("29 9 -", 20),
    ("583 33 -", 550),
    ("1 1 -", 0),
    ("-126 24 -", -150),
    ("987654321 123456789 -", 864197532),
    ("-987654321 123456789 -", -1111111110),

    ("1 0 *", 0),
    ("3 3 *", 9),
    ("120 20", 2400),
    ("-1 1 *", 0),
    ("5 -6 *", -30),
    ("9876543 123456 *", 451149483006),
    ("-987654 123456 *", -451149483006),

    ("0 1 /", 0),
    ("20 4 /", 5),
    ("1266 3 /", 422),
    ("0 -1 /", 0),
    ("-1266 3 /", -422),
    ("987654322 2 /", 493827161),
    ("-987654322 2 /", -493827161),

    ("0 sin", 0),
    ("1 sin", 0.8414709848),
    ("-1 sin", -0.8414709848),
    ("43 sin", -0.83177474262),
    ("-43 sin", 0.83177474262),
    ("90 sin", 0.8939966636),
    ("25.369 sin", 0.23406697384),
    ("-12398.236 sin", -0.9982358998),
    ("9861236 sin", 0.28263495415),

    ("0 cos", 1),
    ("1 cos", 0.54030230586),
    ("-1 cos", 0.54030230586),
    ("43 cos", 0.55511330152),
    ("-43 cos", 0.55511330152),
    ("90 cos", -0.44807361612),
    ("25.369 cos", 0.97222047487),
    ("-12398.236 cos", 0.05937245447),
    ("9861236 cos", -0.95922754479),

    ("0 _ 1", 0),
    ("1 _ 1", 1),
    ("43 _ 5", 2.121747460841898),
    ("100 _ 2", 10),
    ("875564896227 _ 1", 875564896227),
    ("1235.563 _ 1.2", 377.1847094765633),
    ("59872369.547896589 _ 11.369", 4.83140055442166),

    ("0 ^ 1", 0),
    ("1 ^ 1", 1),
    ("1 ^ 0", 0),
    ("43 ^ 2", 1849),
    ("100 ^ 3", 1000000),
    ("-2 ^ -1", -0.5),
    ("2 ^ 11", 2048),
    ("1.678 ^ 5.963", 21.89951196284224),

    ("0 1 / 1 + 1 -", 0),
    ("20 4 / 4 * 20 -", 0),
    ("1266 3 / 78 +", 500),
    ("0 -1 / 1 + 1 -", 0),
    ("-1266 3 / 78 -", -500),
    ("0 sin 1 + 0 cos +", 2),
    ("43 sin 69.69 + 1 cos +", 69.3985275632),
    ("100 sin 3 / 33.852 cos -", 0.59248644973),
    ("987654322 2 / 827161 - 7000000 +", 500000000),
    ("-987654322 2 / 827161 - 7000000 -", -500000000),
    ("987654322 2 / 827161 - 7000000 + 0 ^ 1 +", 500000000),
    ("-987654322 2 / 827161 - 7000000 - 43 ^ 2 -", -500001849)

])
def test_postfix_conversion(problem, result):
    assert MathLib.solve_postfix_equation(problem) == result


@pytest.mark.parametrize("problem", [
    ("velký špatný"),
    ("1 0 /"),
    ("-1 0 /"),
    ("0 1 + +"),
    ("0 1 / /"),
    ("-1 _"),
    ("-0.8745 _"),
    ("55sadf 2 /"),
    ("54fa 2 *"),
    ("87aef7 +"),
    ("-78sf885 2 -")
])
def test_bad_input(problem):
    result_of_mathlib = MathLib.solve_postfix_equation(problem)
    assert result_of_mathlib is None
