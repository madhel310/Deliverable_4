class Fraction: 
    """Represents a fraction and checks or do math with two diffrent fractions."""
    def __init__(self, a: int, b: int):
        """Initialize a fraction with checking if it's only positive value for det denominator, 
        and numerator and denominator are integers."""
        if type(a) is not int or type(b) is not int:
            raise ValueError("Both numerator and denominator must be integers")
        if b <= 0:
            raise ValueError("denominator must be stricktly positive.")

        self.numerator = a
        self.denominator = b


    def __eq__(self, other):
        """Checks if two fractions are equal."""
        if not isinstance(other, Fraction):
            return NotImplemented
        else: 
            return self.numerator * other.denominator == self.denominator * other.numerator        


    def __ne__(self, other):
        """Checks if two fractions are not equal."""
        if not isinstance(other, Fraction):
            return NotImplemented
        else: 
            return self.numerator * other.denominator != self.denominator * other.numerator     


    def __lt__(self, other):
        """Checks if fraction is lesser than other fraction."""
        if not isinstance(other, Fraction):
            return NotImplemented
        else: 
            return self.numerator * other.denominator < self.denominator * other.numerator     


    def __le__(self, other):
        """Checks if fraction is lesser than other or equal fraction."""
        if not isinstance(other, Fraction):
            return NotImplemented
        else: 
            return self.numerator * other.denominator <= self.denominator * other.numerator  


    def __gt__(self, other):
        """Checks if fraction is greater than other fraction. """
        if not isinstance(other, Fraction):
            return NotImplemented
        else: 
            return self.numerator * other.denominator > self.denominator * other.numerator  


    def __ge__(self, other):
        """Checks if fraction is greater than other or equal fraction."""
        if not isinstance(other, Fraction):
            return NotImplemented
        else: 
            return self.numerator * other.denominator >= self.denominator * other.numerator  


    def __mul__(self, other):
        """Multiplies the two fractions together."""
        if not isinstance(other, Fraction):
            return NotImplemented
        else: 
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)


    def __add__(self, other):
        """Add's the two fractions together."""
        if not isinstance(other, Fraction):
            return NotImplemented
        else: 
            return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                            self.denominator * other.denominator)


    def __sub__(self, other):
        """Subtract the two fractions together."""
        if not isinstance(other, Fraction):
            return NotImplemented
        else: 
            return Fraction(self.numerator * other.denominator - self.denominator * other.numerator,
                            self.denominator * other.denominator)


    def __truediv__(self, other):
        """Divides the two fractions together."""
        if not isinstance(other, Fraction):
            return NotImplemented
        if (self.denominator * other.numerator) == 0:
            raise ZeroDivisionError("cannot divide by zero")
        if other.numerator < 0:
            return Fraction(-(self.numerator * other.denominator), -(self.denominator * other.numerator))
        else: 
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

