"""
[완전탐색_순열]
"""

def nPr(k, n, r, nums):
    if k == r:
        nums.add(tuple(box))
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                box[k] = arr[i]
                nPr(k+1, n, r, nums)
                visited[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
box = [0] * M
visited = [0] * N
nums = set()
nPr(0, N, M, nums)
nums = list(nums)
nums.sort()

for i in nums:
    print(*i)