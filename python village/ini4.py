a = 4688
b = 9537
oddSum = 0

for i in range(a, b+1):
    if i % 2 == 1:
        oddSum = oddSum + i

print(oddSum)
