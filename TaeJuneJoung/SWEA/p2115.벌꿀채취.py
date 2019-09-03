def oneso(di, dj, work):
    global idx
    for i in range(1, 1 << M):
        temp = 0
        s = 0
        for j in range(M):
            if i & (1 << j) != 0:
                s += box[j]
                temp += box[j]**2
                if s > C:
                    break
        if s <= C:
            if temp > maxV[work]:
                maxV[work] = temp
                idx = (di, dj)

T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    work_set = set()
    maxV = [0, 0]
    idx = 0
    for work in range(2):
        for i in range(N):
            if not i in work_set:
                for j in range(N):
                    if j+M <= N:
                        box = []
                        for m in range(M):
                            box.append(arr[i][j+m])
                        oneso(i, j, work)
        work_set.add(idx[0])

    print("#{} {}".format(t, sum(maxV)))