def fibonacci_memo(n, memo):
    if n <= 1:
        return n
    if memo[n] is None:
        memo[n] = fibonacci_memo(n, memo) + fibonacci_memo(n-1, memo)
    return memo[n]
