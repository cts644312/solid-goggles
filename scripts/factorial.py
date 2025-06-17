# Simple Python script to test SonarCloud analysis

def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """Main function to test the factorial function."""
    sample_input = 5
    result = factorial(sample_input)
    print(f"The factorial of {sample_input} is {result}")

if __name__ == "__main__":
    main()
