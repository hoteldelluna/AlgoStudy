# SW Expert 1873. 상호의 배틀필드

'''

그냥 입력이 된대로 동작되도록 했다.

'''


def shoot():
    global si, sj
    if field[si][sj] == di[0]:  # 위로 사격
        for i in range(si, -1, -1):
            if field[i][sj] == "*":  # 벽돌 일때
                field[i][sj] = "."
                return
            elif field[i][sj] == "#":  # 강철벽 일때
                return
    elif field[si][sj] == di[1]:  # 아래로 사격
        for i in range(si, H):
            if field[i][sj] == "*":
                field[i][sj] = "."
                return
            elif field[i][sj] == "#":
                return
    elif field[si][sj] == di[2]:  # 왼쪽으로 사격
        for j in range(sj, -1, -1):
            if field[si][j] == "*":
                field[si][j] = "."
                return
            elif field[si][j] == "#":
                return
    else:                       # 오른쪽으로 사격
        for j in range(sj, W):
            if field[si][j] == "*":
                field[si][j] = "."
                return
            elif field[si][j] == "#":
                return


def move(n):
    global si, sj
    if n == "U":    # 위로 이동
        field[si][sj] = "^"
        if si >= 1 and field[si-1][sj] == ".":
            field[si][sj], field[si-1][sj] = field[si-1][sj], field[si][sj]
            si -= 1
            return
    elif n == "D":  # 아래로 이동
        field[si][sj] = "v"
        if si < H-1 and field[si+1][sj] == ".":
            field[si][sj], field[si+1][sj] = field[si+1][sj], field[si][sj]
            si += 1
            return
    elif n == "L":  # 왼쪽으로 이동
        field[si][sj] = "<"
        if sj >= 1 and field[si][sj-1] == ".":
            field[si][sj], field[si][sj-1] = field[si][sj-1], field[si][sj]
            sj -= 1
            return
    else:           # 오른쪽으로 이동
        field[si][sj] = ">"
        if sj < W-1 and field[si][sj+1] == ".":
            field[si][sj], field[si][sj+1] = field[si][sj+1], field[si][sj]
            sj += 1
            return


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    N = int(input())
    order = input()
    si = 0
    sj = 0
    di = "^v<>"

    for i in range(H):      # 시작 위치 찾기
        for j in range(W):
            if field[i][j] in di:
                si = i
                sj = j

    for n in order:     # 명령대로 동작하기
        if n == "S":
            shoot()
        else:
            move(n)

    print("#{}".format(tc), end=" ")
    for i in field:
        print(''.join(i))