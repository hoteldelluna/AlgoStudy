"""
[완전탐색_조합]
"""

def nCr(n, r):
    global minV
    if r == 0:
        A, B = 0, 0
        copy_food = [i for i in range(N)]
        copy_food.remove(box[-1])
        for i in range(N//2 -1):
            copy_food.remove(box[i])
            for j in range(i+1, N//2):
                A += arr[box[i]][box[j]]
                A += arr[box[j]][box[i]]
        
        for i in range(N//2):
            for j in range(i+1, N//2):
                B += arr[copy_food[i]][copy_food[j]]
                B += arr[copy_food[j]][copy_food[i]]
        
        minV = min(minV, abs(A - B))

    elif n < r:
        return
    else:
        box[r-1] = food[n-1]
        nCr(n-1, r-1)
        nCr(n-1, r)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    food = [i for i in range(N)]
    box = [0] * (N//2)
    check = [0] * N

    minV = 987654321
    nCr(N, N//2)
    print(f"#{t} {minV}")