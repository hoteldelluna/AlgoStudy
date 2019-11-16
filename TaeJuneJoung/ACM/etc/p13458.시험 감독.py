N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# 총감독은 방마다 한 명씩은 있어야한다.
result = N
for a in A:
    a = a - B
    if a > 0:
        if a % C:
            result += (a // C) +1
        else:
            result += a // C
print(result)
