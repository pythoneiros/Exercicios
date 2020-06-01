arr = list(map(int, input().split()))

n = int(input())

rotacao = n % len(arr)

arr = arr[-rotacao:] + arr[:-rotacao]


print(arr)
