"""
소수 판별 - `아리스토네스의 체`를 이용
"""

primary = []
visited = [0] * 1001

for num in range(2, 1001):
    if visited[num] == 0:
        primary.append(num)
        for i in range(num, 1001, num):
            visited[i] = 1

cnt = 0

N = int(input())
arr = list(map(int, input().split()))

for num in arr:
    if num in set(primary):
        cnt += 1

print(cnt)