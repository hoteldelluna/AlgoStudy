"""
[완전탐색]
1~9까지의 범위, 100의 자리수, 다른 숫자값을 가짐
주어진 strick와 ball의 값을 맞춰가며 최종값이 다르다면 Pass
같다면 cnt++

정확한 의미를 파악하지 못한 문제로 다시 풀어볼 것!
"""

T = int(input())
arr = [[0] * 5 for i in range(T)]
for t in range(T):
	N, strick, ball = map(int, input().split())
	arr[t][0] = N//100
	arr[t][1] = N%100//10
	arr[t][2] = N%10
	arr[t][3] = strick
	arr[t][4] = ball

cnt = 0
for i in range(1, 10):
	for j in range(1, 10):
		if i == j: continue
		for k in range(1, 10):
			if i == k or j == k: continue
			isPossible = True
			for t in range(T):
				strick = 0
				ball = 0
				if i == arr[t][0]:
					strick += 1
				elif i == arr[t][1] or i == arr[t][2]:
					ball += 1
				if j == arr[t][1]:
					strick += 1
				elif j == arr[t][0] or j == arr[t][2]:
					ball += 1
				if k == arr[t][2]:
					strick += 1
				elif k == arr[t][0] or k == arr[t][1]:
					ball += 1
				
				if not(strick == arr[t][3] and ball == arr[t][4]):
					isPossible = False
					break
			if isPossible:
				cnt += 1
print(cnt)