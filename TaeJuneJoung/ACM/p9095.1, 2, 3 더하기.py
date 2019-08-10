"""[BFS || DP]
[BFS]
각 노드들이 접근하여 해당 값을 만든 순서를 만들면 되겠다고 생각
가중치가 없는 것을 보니 BFS로 풀릴 것 같았다.

풀고 나서 보니 DP로 푼적이 있었다.
현재 문제에서는 시간차가 없지만,
영역이 컷다면 DP로 풀어야할 것 같다.

[DP]
규칙성을 본다면
DP[N+3] = DP[N] + DP[N+1] + DP[N+2]
"""

#[BFS]
nums = [1, 2, 3]
def sum_value(start, N, cnt):
	q = [0]
	while q:
		k = q.pop()
		for i in range(len(nums)):
			x = k + nums[i]
			if x >= 0 and x < N:
				q.append(x)
			if x == N:
				cnt += 1
	return cnt

T = int(input())
for t in range(T):
	N = int(input())
	cnt = 0
	print(sum_value(0, N, cnt))

#[DP]
# num = 11
# DP = [0] * num
# DP[1] = 1
# DP[2] = 2
# DP[3] = 4

# for i in range(4, num):
# 	DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

# T = int(input())
# for t in range(T):
# 	N = int(input())
# 	print(DP[N])