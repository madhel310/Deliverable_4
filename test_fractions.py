import pytest 


from fraction import Fraction


def test_valid_init():
    """Test that valid numerator and denominator values are stored correctly."""
    fraction = Fraction(5, 3)

    assert fraction.numerator == 5
    assert fraction.denominator == 3


def test_invalid_init():
    """Test that negative and zero denominators raise ValueError."""
    with pytest.raises(ValueError):
        Fraction(5, -3)

    with pytest.raises(ValueError):
        Fraction(5, 0)


def test_equal():
    """Test that equal fractions return true and unequal returns false."""
    assert Fraction(20, 2) == Fraction(10, 1)
    assert not Fraction(5, 2) == Fraction(3, 2)
        

def test_not_equal():
    """Test that unequal fractions return true and equal returns false."""
    assert Fraction(7, 2) != Fraction(10, 1) 
    assert not Fraction(20, 2) != Fraction(10, 1)
        

def test_less_than():
    """Test that a smaller fraction returns true and larger fraction returns false."""
    assert Fraction(7, 2) < Fraction(10, 1) 
    assert not Fraction(10, 2) < Fraction(3, 1)


def test_less_than_or_equal():
    """Test that a smaller or equal fraction returns true and larger fraction returns false."""
    assert Fraction(7, 2) <= Fraction(10, 1) 
    assert not Fraction(12, 1) <= Fraction(1, 1)


def test_greater_than():
    """Test that a larger fraction returns true and smaller fraction returns false."""
    assert Fraction(5, 1) > Fraction(2, 1)
    assert not Fraction(1, 1) > Fraction(10, 1)


def test_greater_than_or_equal():
    """Test that a larger or equal fraction returns true and smaller fraction returns false"""
    assert Fraction(10, 2) >= Fraction(3, 2)
    assert not Fraction(1, 1) >= Fraction(7, 1)


def test_multiplication():
    """Test that multiplying two fractions gives correct answer."""
    output = Fraction(1, 2) * Fraction(1, 2)

    assert output == Fraction(1, 4)


def test_addition():
    """Test that adding two fractions gives correct answer."""
    output = Fraction(1, 2) + Fraction(1, 2)

    assert output == Fraction(2, 2)


def test_subtraction():
    """Test that subtracting two fractions gives correct answer."""
    output = Fraction(7, 4) - Fraction(3, 4)

    assert output == Fraction(4, 4)

def test_division():
    """Test that dividing two fractions gives correct answer."""
    output = Fraction(1, 2) / Fraction(1, 2)

    assert output == Fraction(1, 1)


def test_division_by_zero():
    """Test that dividing with zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / Fraction(0, 2) 

