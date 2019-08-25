"""
[완전탐색:Brute-force Search]
집합의 모든 원소의 집합을 꺼내서 합한 후,
해당 값과 같은지 비교하여 같으면 cnt++
"""

N, R = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, 1 << N):
    sum_num = 0
    for j in range(N):
        if i & 1 << j != 0:
            sum_num += arr[j]
    if sum_num == R:
        cnt += 1
print(cnt)