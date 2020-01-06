NUMBERS = [0] * 10

N = input()

for i in N:
    NUMBERS[int(i)] += 1

value = NUMBERS[6] + NUMBERS[9]
maxV = value//2+1 if value%2 else value//2
for i in range(len(NUMBERS)):
    if i == 6 or i == 9:
        pass
    else:
        maxV = NUMBERS[i] if NUMBERS[i] > maxV else maxV

print(maxV)