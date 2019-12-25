T = int(input())
for t in range(1, T+1):
    A, B, C = map(int, input().split())
    minV = min(A, B)
    maxN = C // minV
    print(f'#{t} {maxN}')