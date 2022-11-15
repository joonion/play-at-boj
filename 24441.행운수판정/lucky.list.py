n = 10 ** 6
s = list(range(1, n + 1, 2))
i = 1
while i < len(s):
    k = s[i]
    del s[k-1::k]
    i += 1

print(f"#define LEN_LUCKY {len(s)}")
print("const int lucky[] = {")
print(",".join(map(str, s)))
print("};")
