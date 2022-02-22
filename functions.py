def fibonacci(num_of_terms=1):
    output = []
    for idx in range(num_of_terms):
        if idx == 0 or idx == 1:
            output.append(1)
        else:
            output.append(output[idx - 1] + output[idx - 2])
    return output

def prime_numbers(limit):
    primes = []
    filter = [True] * (limit + 1)
    for i in range(2, limit+1):
        if filter[i]:
            primes.append(i)
            # now set all the multiples of i to False in filter because they are not primes
            for f in range(i, limit+1, i):
                filter[f] = False
        
    return primes

    
        
