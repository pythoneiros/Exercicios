par = []
impar = []

n = int(input())

for i in range(n):
    x = input()
    par.append(x) if int(x) % 2 == 0 else impar.append(x)

print("Par".center(10))
print(' '.join(par))
print("Impar".center(10))
print(' '.join(impar))
