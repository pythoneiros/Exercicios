# -*- coding: utf-8 -*-

elements = str(input("Type the elements of list: ")).split()
elements = list(map(float,elements))

times = int(input("How many times you wish shift to right: "))

for _ in range(times):
	removed = elements.pop()
	elements.insert(0,removed)

print(elements)