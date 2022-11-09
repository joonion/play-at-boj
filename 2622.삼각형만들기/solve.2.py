from math import ceil
n = int(input())
cnt = 0
for x in range(ceil(n/3), ceil(n/2)):
    for y in range(ceil((n - x)/2), x + 1):
        cnt += 1
print(cnt)