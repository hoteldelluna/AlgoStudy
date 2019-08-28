"""
[시뮬레이션_완전탐색&조합]
1. 집과 치킨의 거리를 구해서 값들을 이중리스트에 차곡 차곡 넣어줌
2. 주어진 숫자만큼 치킨집만 영업을 해야하기에 조합을 이용하여 최소값을 찾아줌
"""

def check(i, j, home_cnt):
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1:
                X = i - x
                Y = j - y
                if X < 0:
                    X = -X
                if Y < 0:
                    Y = -Y
                distance_list[chicken_cnt][home_cnt] = X + Y
                home_cnt += 1

def nCr(n, r, min_value):
    if r == 0:
        value_list = [987654321] * home
        for i in box:
            sum_value = 0
            for j in range(home):
                if distance_list[i][j] < value_list[j]:
                    value_list[j] = distance_list[i][j]
            for k in value_list:
                sum_value += k
        min_value = min_value if min_value < sum_value else sum_value
        min_list.append(min_value)
    elif n < r:
        return
    else:
        box[r-1] = matrix[n-1]
        nCr(n-1, r-1, min_value)
        nCr(n-1, r, min_value)

N, M = map(int, input().split())
arr = [0] * N
home = 0
chicken = 0
for t in range(N):
    arr[t] = list(map(int, input().split()))
    for i in arr[t]:
        if i == 1:
            home += 1
        elif i == 2:
            chicken += 1

distance_list = [[0] * home for i in range(chicken)]

home_cnt = 0
chicken_cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            distance = check(i, j, home_cnt)
            chicken_cnt += 1

box = [0] * M
matrix = [i for i in range(chicken)]
min_value = 987654321
min_list = []
nCr(chicken, M, min_value)

print(min(min_list))