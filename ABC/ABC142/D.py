A, B = map(int, input().split())

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

a_fact = set(prime_factorize(A))
b_fact = set(prime_factorize(B))
fact = a_fact & b_fact
print(len(fact) + 1)

        