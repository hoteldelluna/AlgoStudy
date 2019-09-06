#0:상, 1:하, 2:좌, 3:우
dx = [0, 0, -1, 1]
dy = [1, -1, 0 ,0]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    oneja = [0] * N
    #x:x축방향, y:y축방향, d:방향, e:에너지
    #d -> 0:상, 1:하, 2:좌, 3:우
    for i in range(N):
        x, y, d, e = map(int, input().split())
        #0.5초를 처리하기 위해 맵을 2배 처리
        x, y = 2*x, 2*y
        oneja[i] = [x, y, d, e]
    
    oneja_cnt = N
    energe = 0

    #move_oneja: 원자가 움직인 것을 담는 리스트
    #oneja_crush: 충돌한 원자를 담는 집합(단, 중복 충돌도 담아버림)
    #energe_crush: 충돌 원자만 담는 집합(중복 없음)
    while oneja_cnt:
        move_oneja = [0] * oneja_cnt
        oneja_crush = set()
        energe_crush = set()
        for i in range(oneja_cnt):
            x, y, d, e = oneja[i]
            x += dx[d]
            y += dy[d]
            move_oneja[i] = [x, y, d, e]

            oneja_cursh_cnt = len(oneja_crush)
            oneja_crush.add((x,y))

            if oneja_cursh_cnt == len(oneja_crush):
                energe_crush.add((x,y))
            
        oneja = []

        for i in range(oneja_cnt):
            x, y, d, e = move_oneja[i]
            if (x, y) in energe_crush:
                energe += e
                oneja_cnt -= 1
            elif max(x, y) > 2000 or min(x, y) < -2000:
                oneja_cnt -= 1
            else:
                oneja.append([x, y, d, e])

    print(f"#{t} {energe}")
