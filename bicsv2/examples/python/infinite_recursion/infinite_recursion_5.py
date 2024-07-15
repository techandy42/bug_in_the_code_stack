def permute(a, l, r):
    if l == r:
        print(''.join(a))
        permute(a, l, r)
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]
