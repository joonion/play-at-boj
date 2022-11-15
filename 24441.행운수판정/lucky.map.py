n = 10 ** 6
s = list(range(1, n + 1, 2))
i = 1
while i < len(s):
    k = s[i]
    del s[k-1::k]
    i += 1

b = ["0"] * (n + 1)
for n in s:
    b[n] = "1"

print("const unsigned int lucky[] = {")
for i in range(0, len(b) + 1, 32):
    print(int("".join(b[i:i+32]), 2), end=",")
print("};")
