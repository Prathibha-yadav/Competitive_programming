def is_prime(n):
    if n <= 1:
        return "not prime"
    for i in range(2, int(n**0.5) + 1):
        print(i)
        if n % i == 0:
            
            return "not prime"
    return "prime"

n = int(input())
res = is_prime(n)
print(res)
