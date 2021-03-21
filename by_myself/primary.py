#!/usr/bin/env python3

print("hoge")

def trial_devision(n):
    org_n = n
    if n < 2:
        return []
    
    prime_factors = []

    for i in range(2, int(n**0.5)+1):  # n/2 is easy to explain
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 1 and n != org_n:
        prime_factors.append(n)
    return prime_factors

def is_primary(n):
    return len(trial_devision(n)) == 0
        

if __name__ == '__main__':
    for n in range(10):
        print(f"{n} : {is_primary(n)}")
        # print(trial_devision(n))
