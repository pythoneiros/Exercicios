# -*- coding : utf-8 -*-

groups = []

elements = str(input("Type elements of list: ")).split()
elements = list(map(int,elements))

quantity_groups = int(input("Split in how many groups : "))

each_group = len(elements) // quantity_groups

current_index = 0

while current_index < len(elements):

	group = elements[ current_index : each_group + current_index]

	groups.append(group)

	current_index += each_group

print(groups)