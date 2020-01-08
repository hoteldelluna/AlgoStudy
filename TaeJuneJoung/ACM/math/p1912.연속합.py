N = int(input())
V = [0] * (N+1)

arr = [0]
arr += list(map(int, input().split()))

maxV = -1001

for i in range(1, N+1):
    V[i] = max(V[i-1] + arr[i], arr[i])
    maxV = max(maxV, V[i])

print(maxV)