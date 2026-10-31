star = '* '
star2 = '*'
h = int(input())
n = int(input())

for i in range(n):
    for j in range(1, h+1):
        print(star*(j-1), star2, sep='')
    h += 1