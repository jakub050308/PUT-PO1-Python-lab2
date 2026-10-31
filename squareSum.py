x, y = input().split()
sum = 0
for i in range(int(x), int(y)+1):
    sum = i ** 2 + sum
print(sum)