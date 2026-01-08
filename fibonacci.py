def fibonacci_memoized(n, memo={}):
    """Compute the nth Fibonacci number using memoization."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

print("Fibonacci numbers (memoized):")
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci_memoized(i)}")