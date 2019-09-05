"""
[시뮬레이션]
제한시간 초과가 발생하여,
새로운 리스트로 담아 처리함
"""

dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

T = int(input())
for t in range(1, T+1):
	N, M, K = map(int, input().split())
	group = [0] * K
	for i in range(K):
		group[i] = list(map(int, input().split()))
	while M:
		for i in range(len(group)):
			y, x, c, d = group[i]
			y += dy[d]
			x += dx[d]
			if y == 0 or x == 0 or y == N-1 or x == N-1 and x > -1:
				c = c//2
				if c == 0:
					y = x = -1
					d = 0
				else:
					if d == 4:
						d = 3
					elif d == 1:
						d = 2
					elif d == 2:
						d = 1
					elif d == 3:
						d = 4
			group[i] = [y, x, c, d]

		group.sort(key=lambda g:g[2], reverse=True)
		copy_group = []
		for i in range(len(group)):
			for j in range(i+1, len(group)):
				if group[i][0] == group[j][0] and group[i][1] == group[j][1]:
						group[i][2] += group[j][2]
						group[j][2] = 0
						group[j][3] = group[i][3]
			if group[i][2] != 0:
				copy_group.append(group[i])
		
		group = copy_group[:]
		
		M -= 1

	sum_cell = 0
	for i in range(len(group)):
		sum_cell += group[i][2]

	print(f"#{t} {sum_cell}")

