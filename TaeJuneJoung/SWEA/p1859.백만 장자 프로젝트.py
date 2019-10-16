T = int(input())

for t in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))
    maxV = M[N-1]
    sumV = 0
    for i in range(N-2, -1, -1):
        if M[i] < maxV:
            sumV += (maxV - M[i])
        else:
            maxV = M[i]

    print(f"#{t} {sumV}")