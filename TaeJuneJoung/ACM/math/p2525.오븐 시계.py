A, B = map(int, input().split())
C = int(input())

minute = B + C

if minute >= 60:
    A += minute // 60
    minute %= 60

if A >= 24:
    A -= 24

print(A, minute)