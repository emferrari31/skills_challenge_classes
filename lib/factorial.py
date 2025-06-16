def factorial(n):
    product = n
    while n > 1:
        n -= 1
        product *= n
    return product

print(f"""
Running: factorial(5)
Expected: 120
Actual: {factorial(5)}
""")

print(f"""
Running: factorial(3)
Expected: 6
Actual: {factorial(3)}
""")

print(f"""
Running: factorial(7)
Expected: 5040
Actual: {factorial(7)}
""")
