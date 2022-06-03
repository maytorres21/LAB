def prod(m, n):
    if not n:
        return 0
    else:
        return m + prod(m, n - 1)


for x, y in [(12, 2),
             (23, 6),
             (100, 10)
             ]:
    print(f'The product of {x} and {y} is {prod(x, y)}')
