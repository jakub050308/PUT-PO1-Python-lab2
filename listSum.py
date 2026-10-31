list = input().split()
i, j = input().split()
i = int(i)
j = int(j)
sum = 0
for i in range(i, j+1):
    sum += int(list[i])

print(sum)