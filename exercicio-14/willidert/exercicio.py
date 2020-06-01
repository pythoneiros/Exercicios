def is_pow(a, b):
    for i in range(a):
        if b**i == a:
            return True
        elif b**i > a:
            return False


a, b = map(int, input().split())
print(is_pow(a, b))
