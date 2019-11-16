"""
문제의 입력 부분에서
'둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 지도의 각 칸에 쓰여 있는 수는 10을 넘지 않는 자연수 또는 0이다.'
부분이 이해되지 않아 참고하여 풀음

참고 사이트
https://dongsik93.github.io/algorithm/2019/11/12/algorithm-boj-14499/
"""

def move_able(m):
    global isPrint
    di = x + dx[m]
    dj = y + dy[m]
    if 0 <= di < N and 0 <= dj < M:
        isPrint = True
        return True
    else:
        return False

def copy(m):
    if arr[x+dx[m]][y+dy[m]] == 0:
        #이동한 칸이 0이면 주사위 바닥면의 숫자 복사
        arr[x+dx[m]][y+dy[m]] = dice[0]
    else:
        #이동한 칸이 0이 아니면,
        #주사위 바닥면의 숫자는 이동칸의 숫자를 가지고
        #이동칸의 숫자는 0으로 변경
        dice[0] = arr[x+dx[m]][y+dy[m]]
        arr[x+dx[m]][y+dy[m]] = 0

N, M, x, y, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
move = list(map(int, input().split()))
"""
주사위 전면도(숫자: dice index)
-> 0은 주사위 밑면, 1은 윗면

  2
4 1 3
  5
  0
"""
dice = [0] * 6
#dice[0] = 주사위 밑바닥
dice[0] = arr[x][y]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
isPrint = False

# m 1: 동, 2: 서, 3: 북, 4: 남
for m in move:
    if move_able(m):
        if m == 1:
            dice[1], dice[3], dice[4], dice[0] = dice[4], dice[1], dice[0], dice[3]
        elif m == 2:
            dice[1], dice[3], dice[4], dice[0] = dice[3], dice[0], dice[1], dice[4]
        elif m == 3:
            dice[2], dice[1], dice[5], dice[0] = dice[1], dice[5], dice[0], dice[2]
        else:
            dice[2], dice[1], dice[5], dice[0] = dice[0], dice[2], dice[1], dice[5]
        copy(m)
    if isPrint:
        #윗면 print
        print(dice[1])
        isPrint = False
        x += dx[m]
        y += dy[m]