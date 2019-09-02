"""
[완전탐색_재귀]
"""
def f(n, s): #n월, s: n-1월까지의 사용금액
    global minV
    if n >= 13:
        if minV > s:
            minV = s
    else:
        f(n+1, s+d*table[n])
        f(n+1, s+m)
        f(n+3, s+m3)

T = int(input())
for t in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    table = [0] + list(map(int, input().split()))
    minV = y

    f(1, 0)
    print('#{} {}'.format(t, minV))


"""
[DP]
"""
for t in range(1, int(input())+1):
	d, m, m3, y = map(int, input().split())
	table = list(map(int, input().split()))
	minV = y
	DP = [0] * 13

	for i in range(1, 13):
		if i > 2:
			DP[i] = min(DP[i-3] + m3, DP[i-1] + min(d*table[i-1], m))
		else:
			DP[i] = DP[i-1] + min(d*table[i-1], m)

	minV = minV if minV < DP[-1] else DP[-1]
	print(f"#{t} {minV}")
