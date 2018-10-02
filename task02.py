# Task 02
# Function to calculate Fibonacci numbers

"""
Anton:
See the comments from the first branch.
"""

if __name__ == "__main__":
    def fib(n):
        """Calculate first n elements of Fibonacchi sequence."""
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    n = 8

    for i in range(n):
        print(fib(i))
