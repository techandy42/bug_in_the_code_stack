def gcd(a, b):
    while True:
        if b == 0:
            return b
        temp = a
        a = b
        b = temp % b
