# -*- coding : utf-8 -*-

def multiplier(couple):
    mult = 1;

    for num in couple:
        mult *= num

    return mult

def is_power(value,power):

    results = []
    divisor = power
    original_value = value

    if value <= 0:
        raise ValueError("Invalid Value")
    else:
        while True:
            if value >= divisor:
                
                if value % divisor == 0:
                    results.append(divisor)
                    value //= divisor
                else:
                    divisor += 1
            else:
                break

    requisitos = []

    # A multiplicação dos divisores ser igual à potência digitada
    requisitos.append( original_value == multiplier(results) )
    
    # Só existir elementos iguais dentro da lista
    requisitos.append( len(set(results)) == 1)

    # Retorna se todos os requisitos retornaram true
    return all(requisitos)

assert is_power(16,2) == True
assert is_power(2,2)  == True
assert is_power(27,3) == True
assert is_power(81,9) == True
assert is_power(12,4) == False
assert is_power(15,3) == False