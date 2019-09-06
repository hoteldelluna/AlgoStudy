di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def shoot(i, j, d):
	y, x = i, j
	while True:
		y += di[d]
		x += dj[d]
		if 0 <= x < W and 0 <= y < H:
			if arr[y][x] == '#':
				return
			elif arr[y][x] == '*':
				arr[y][x] = '.'
				return
		else:
			return

T = int(input())
for t in range(1, T+1):
	H, W = map(int, input().split())
	arr = [list(map(str, input())) for _ in range(H)]
	N = int(input())
	C = input() #Command

	tank = '^>v<'
	tank_dir = {'^': 0, '>': 1, 'v': 2, '<': 3}
	for i in range(H):
		for j in range(W):
			if arr[i][j] in tank:
				tank_idx = [i, j, tank_dir[arr[i][j]]]
				arr[i][j] = '.'

	move = 'URDL' #방향을 해당 방향으로 바꾸고, 전진 가능하면 전진
	for i in range(N):
		if C[i] == 'S':
			shoot(tank_idx[0], tank_idx[1], tank_idx[2])
		else:
			for j in range(len(move)):
				if C[i] == move[j]:
					my = tank_idx[0]+di[j]
					mx = tank_idx[1]+dj[j]
					if 0 <= my < H and 0 <= mx < W:
						if arr[my][mx] == '.':
							tank_idx[0] += di[j]
							tank_idx[1] += dj[j]
					tank_idx[2] = j
	arr[tank_idx[0]][tank_idx[1]] = tank[tank_idx[2]]
	print("#"+str(t), end=" ")
	for i in range(len(arr)):
		print(''.join(arr[i]))