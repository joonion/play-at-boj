s = list(range(1, 10**6, 2))
i = 1
while i < len(s):
    k = s[i]
    del s[k-1::k]
    i+=1

import sys
input = sys.stdin.readline

S = set(s)
for _ in range(int(input())):
    N = int(input())
    print("lucky" if N in S else "unlucky")
    