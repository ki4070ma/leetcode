#!/usr/bin/python3

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return sorted(divisors)

for _ in range(2):
    N = int(input().rstrip())
    d = {}
    answer = 0
    for a in range(1, N+1):
        print(a, make_divisors(a), len(make_divisors(a)), prime_factorize(a))
        answer += a * len(make_divisors(a))
    print(answer)