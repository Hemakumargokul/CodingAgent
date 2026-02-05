"""
Comprehensive tests for the calculator module.
"""

import pytest
from calculator import Calculator, factorial, is_prime, fibonacci


class TestCalculator:
    """Test cases for the Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        assert self.calc.add(2, 3) == 50
        assert self.calc.add(10, 20) == 30
        assert self.calc.add(0.5, 0.3) == pytest.approx(0.8)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert self.calc.add(-2, -3) == -5
        assert self.calc.add(-10, 5) == -5
        assert self.calc.add(10, -5) == 5
    
    def test_add_zero(self):
        """Test addition with zero."""
        assert self.calc.add(0, 5) == 5
        assert self.calc.add(5, 0) == 5
        assert self.calc.add(0, 0) == 0
    
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(10, 10) == 0
        assert self.calc.subtract(3, 5) == -2
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.subtract(-5, 3) == -8
        assert self.calc.subtract(5, -3) == 8
    
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(0.5, 4) == 2.0
        assert self.calc.multiply(7, 7) == 49
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(0, 0) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(-2, -3) == 6
        assert self.calc.multiply(2, -3) == -6
    
    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        assert self.calc.divide(6, 2) == 3
        assert self.calc.divide(10, 4) == 2.5
        assert self.calc.divide(1, 3) == pytest.approx(0.3333333333333333)
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert self.calc.divide(-6, 2) == -3
        assert self.calc.divide(-6, -2) == 3
        assert self.calc.divide(6, -2) == -3
    
    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)
        
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(-5, 0)
    
    def test_power_positive_numbers(self):
        """Test power operation with positive numbers."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 2) == 25
        assert self.calc.power(10, 0) == 1
        assert self.calc.power(2, 0.5) == pytest.approx(1.4142135623730951)
    
    def test_power_negative_base(self):
        """Test power operation with negative base."""
        assert self.calc.power(-2, 2) == 4
        assert self.calc.power(-2, 3) == -8
        assert self.calc.power(-5, 0) == 1
    
    def test_power_negative_exponent(self):
        """Test power operation with negative exponent."""
        assert self.calc.power(2, -1) == 0.5
        assert self.calc.power(4, -2) == 0.0625
        assert self.calc.power(10, -3) == 0.001
    
    def test_square_root_positive_numbers(self):
        """Test square root of positive numbers."""
        assert self.calc.square_root(4) == 2
        assert self.calc.square_root(9) == 3
        assert self.calc.square_root(0) == 0
        assert self.calc.square_root(2) == pytest.approx(1.4142135623730951)
    
    def test_square_root_negative_raises_error(self):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-4)
        
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-1)


class TestFactorial:
    """Test cases for the factorial function."""
    
    def test_factorial_positive_integers(self):
        """Test factorial with positive integers."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
    
    def test_factorial_negative_raises_error(self):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)
        
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-5)
    
    def test_factorial_non_integer_raises_error(self):
        """Test that factorial of non-integer raises TypeError."""
        with pytest.raises(TypeError, match="Factorial is only defined for integers"):
            factorial(2.5)
        
        with pytest.raises(TypeError, match="Factorial is only defined for integers"):
            factorial("5")


class TestIsPrime:
    """Test cases for the is_prime function."""
    
    def test_is_prime_small_primes(self):
        """Test is_prime with small prime numbers."""
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True
        assert is_prime(13) is True
    
    def test_is_prime_small_composites(self):
        """Test is_prime with small composite numbers."""
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False
        assert is_prime(12) is False
    
    def test_is_prime_edge_cases(self):
        """Test is_prime with edge cases."""
        assert is_prime(0) is False
        assert is_prime(1) is False
        assert is_prime(-1) is False
        assert is_prime(-5) is False
    
    def test_is_prime_larger_numbers(self):
        """Test is_prime with larger numbers."""
        assert is_prime(17) is True
        assert is_prime(19) is True
        assert is_prime(23) is True
        assert is_prime(100) is False
        assert is_prime(101) is True
    
    def test_is_prime_non_integer_raises_error(self):
        """Test that is_prime with non-integer raises TypeError."""
        with pytest.raises(TypeError, match="Prime check is only defined for integers"):
            is_prime(2.5)
        
        with pytest.raises(TypeError, match="Prime check is only defined for integers"):
            is_prime("5")


class TestFibonacci:
    """Test cases for the fibonacci function."""
    
    def test_fibonacci_small_sequences(self):
        """Test fibonacci with small sequence lengths."""
        assert fibonacci(0) == []
        assert fibonacci(1) == [0]
        assert fibonacci(2) == [0, 1]
        assert fibonacci(3) == [0, 1, 1]
        assert fibonacci(4) == [0, 1, 1, 2]
        assert fibonacci(5) == [0, 1, 1, 2, 3]
    
    def test_fibonacci_longer_sequences(self):
        """Test fibonacci with longer sequences."""
        expected_10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert fibonacci(10) == expected_10
        
        expected_15 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        assert fibonacci(15) == expected_15
    
    def test_fibonacci_negative_raises_error(self):
        """Test that fibonacci with negative length raises ValueError."""
        with pytest.raises(ValueError, match="Fibonacci sequence length cannot be negative"):
            fibonacci(-1)
        
        with pytest.raises(ValueError, match="Fibonacci sequence length cannot be negative"):
            fibonacci(-5)
    
    def test_fibonacci_non_integer_raises_error(self):
        """Test that fibonacci with non-integer raises TypeError."""
        with pytest.raises(TypeError, match="Fibonacci sequence length must be an integer"):
            fibonacci(2.5)
        
        with pytest.raises(TypeError, match="Fibonacci sequence length must be an integer"):
            fibonacci("5")


# Parametrized tests for more comprehensive testing
class TestParametrized:
    """Parametrized tests for comprehensive coverage."""
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
        (100, -50, 50),
        (0.1, 0.2, 0.3),
    ])
    def test_add_parametrized(self, a, b, expected):
        """Parametrized test for addition."""
        calc = Calculator()
        if isinstance(expected, float):
            assert calc.add(a, b) == pytest.approx(expected)
        else:
            assert calc.add(a, b) == expected
    
    @pytest.mark.parametrize("n,expected", [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (25, False),
        (97, True),
    ])
    def test_is_prime_parametrized(self, n, expected):
        """Parametrized test for prime checking."""
        assert is_prime(n) == expected


