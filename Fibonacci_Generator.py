# Fibonacci Generator

print("=== Fibonacci Generator ===")

# User se number of terms lena
n = int(input("Enter the number of terms: "))

# Check for valid input
if n <= 0:
    print("Please enter a positive number.")
else:
    a = 0
    b = 1

    print("\nFibonacci Series:")

    for i in range(n):
        print(a, end=" ")

        # Next Fibonacci number calculate karna
        c = a + b
        a = b
        b = c