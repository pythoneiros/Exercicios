file = open("diario.txt", 'w')

string = input()

while string != 'exit':
    file.write(string + '\n')
    string = input()

file.close()
