"""
`중국인의 나머지 정리`에 대해서 알아보기
"""

# E, S, M = map(int, input().split())

# YEAR = 1

# while True:
#     if (YEAR-E) % 15 == 0 and (YEAR-S) % 28 == 0 and (YEAR-M) % 19 == 0:
#         break
#     YEAR += 1

# print(YEAR)


E, S, M = map(int, input().split())

s = [1, 1, 1]
V = [28*19, 15*19, 15*28]
while True:
    res = (28*19 * s[0]) % 15
    if res == 1:
        V[0] = V[0] * s[0]
        break
    s[0] += 1

while True:
    res = (15*19 * s[1]) % 28
    if res == 1:
        V[1] = V[1] * s[1]
        break
    s[1] += 1

while True:
    res = (15*28 * s[2]) % 19
    if res == 1:
        V[2] = V[2] * s[2]
        break
    s[2] += 1

year = (E*V[0] + S*V[1] + M*V[2]) % (15*28*19)
print(year if year else 7980)