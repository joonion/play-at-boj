def solve(n):
    MAX, MIN = [0] * 3, [0] * 3
    for _ in range(n):
        x, y, z = map(int, input().split())
        p = max(MAX[:2])
        q = max(MAX[1:])
        MAX[0] = x + p
        MAX[1] = y + max(p, q)
        MAX[2] = z + q
        p = min(MIN[:2])
        q = min(MIN[1:])
        MIN[0] = x + p
        MIN[1] = y + min(p, q)
        MIN[2] = z + q
    print(max(MAX), min(MIN))
        
n = int(input())
solve(n)