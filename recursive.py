def fibonacci_recursive(n):
    """Compute the nth Fbonacci number using simple recursion."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
print("Fibonacci numbers (recursive):")
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci_recursive(i)}")