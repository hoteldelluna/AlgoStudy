"""
[완전탐색_순열]
"""

def f(n,k,m,before):
	if(n==m):
		print(*res)
		return
	else:
		for i in range(k):
			if arr[i] >= before:
				before = arr[i]
				res[n] = arr[i]
				f(n+1,k,m,before)

# k = 자리수
# m = 길이
k, m = map(int, input().split())
arr = range(1,k+1)
res = [0] * m
before = 0
f(0,k,m,before)