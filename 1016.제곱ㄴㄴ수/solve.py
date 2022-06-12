def solve(n, m):
    sieve = [1] * (m - n + 1)
    for k in range(2, int(m ** 0.5) + 1):
        s = k * k
        i = (s - (n % s)) % s
        for j in range(i, len(sieve), s):
            sieve[j] = 0
    return sum(sieve)
    
n, m = map(int, input().split())
print(solve(n, m))