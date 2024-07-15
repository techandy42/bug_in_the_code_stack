def power(x, n):
    if n % 2 == 0:
        half_power = power(x, n // 2)
        return half_power * half_power
    else:
        return x * power(x, n - 1)
