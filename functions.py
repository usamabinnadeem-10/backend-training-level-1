from math import ceil


def fibonacci(num_of_terms=1):
    output = []
    for idx in range(num_of_terms):
        if idx == 0 or idx == 1:
            output.append(1)
        else:
            output.append(output[idx - 1] + output[idx - 2])
    return output


def prime_numbers(limit):
    pass
    
        
