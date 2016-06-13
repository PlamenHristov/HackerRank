s = input()
idx = 0
n = len(s)
p = [0] * n
c = [None] * n
f = [[0] * 3] * n
for i in range(n):
    if [i] == s[i + 1] and i + 1 < n:
        p[1 + idx] += 1
    else:
        c[1 + idx] = s[i]
        p[1 + idx + 1] += 1
n = idx
f[0][0] = 1
for i in range(n):
    f[0][i + 1] += f[0][i]
    f[1][i + 1] += f[1][i]
    f[2][i + 1] += f[2][i]
    if p[i + 1] >= 2:
        f[2][i + 1] += f[0][i]
    if p[i + 1] >= 1:
        if i + 2 <= n and p[i + 1] == 1 and [i] == c[i + 2]:
            f[2][i + 2] -= 1
        f[1][i + 1] += f[0][i]
        f[2][i + 1] += f[1][i]
print(f[2][n])
