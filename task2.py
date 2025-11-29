class MathSeries:
    # Constructor to initialize the object with a number 'n'
    def __init__(self, n):
        self.n = n  # Store the number inside the object

    # Recursive factorial function
    def factorial_recursive(self, n):
        # If n is negative, factorial is not possible
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")

        # factorial of 0 or 1 is 1
        if n in (0, 1):
            return 1

        # Recursive call
        return n * self.factorial_recursive(n - 1)

    # Recursive Fibonacci function
    def fibonacci_recursive(self, n):
        # Negative Fibonacci values are not defined
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")

        # Base conditions
        if n == 0:
            return 0
        if n == 1:
            return 1

        # sum of previous two Fibonacci numbers
        return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    # Function to print the full Fibonacci series up to n
    def print_fibonacci_series(self):
        series = []  # Empty list to store Fibonacci numbers

        # Loop from 0 to n and generate Fibonacci numbers
        for i in range(self.n + 1):
            series.append(self.fibonacci_recursive(i))

        return series


if __name__ == "__main__":
    # Input number
    n = 5

    # Create an object of MathSeries class
    math_obj = MathSeries(n)

    # Print factorial using the object
    print("Factorial (recursive):", math_obj.factorial_recursive(n))

    # Print the full Fibonacci series using the object
    print("Fibonacci Series (recursive):", math_obj.print_fibonacci_series())
