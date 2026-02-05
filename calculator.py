"""
A simple calculator module with basic mathematical operations.
"""

class Calculator:
    """A calculator class that performs basic mathematical operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract second number from first number."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide first number by second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Raise base to the power of exponent."""
        return base ** exponent
    
    def square_root(self, number):
        """Calculate square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return number ** 0.5


def factorial(n):
    """Calculate factorial of a non-negative integer."""
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_prime(n):
    """Check if a number is prime."""
    if not isinstance(n, int):
        raise TypeError("Prime check is only defined for integers")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    """Generate the first n numbers in the Fibonacci sequence."""
    if not isinstance(n, int):
        raise TypeError("Fibonacci sequence length must be an integer")
    if n < 0:
        raise ValueError("Fibonacci sequence length cannot be negative")
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence


