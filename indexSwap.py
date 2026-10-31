N, M = input().split()
M = int(M)
tab = input().split()
for i in range(M):
    x, y = input().split()
    x = int(x)
    y = int(y)
    temp = tab[x]
    tab[x] = tab[y]
    tab[y] = temp

print(*tab, sep = ' ')

