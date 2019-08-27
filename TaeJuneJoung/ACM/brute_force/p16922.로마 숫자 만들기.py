"""
[완전탐색_백트래킹]
기존 방식과 같게 풀면 시간초과가 발생하여 규칙성을 찾아 해결
"""

S = set()
N = int(input())
for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            l = N - (i+j+k)
            if i+j+k+l == N and l >-1:
                S.add(i + 5*j + 10*k + 50*l)
print(len(S))

""" 아래와 같게 풀면 시간초과 - 백트래킹 추가하면 가능할련지..."""
# def nPr(r, n, k, s):
#     global cnt
#     if r == k :
#         if s in num_set:
#             return
#         else:
#             num_set.add(s)
#             cnt += 1
#         return
#     else:
#         for i in range(n):
#             box[r] = alpha[i]
#             nPr(r+1, n, k, s+box[r])

# N = int(input())
# alpha = [1, 5, 10 ,50]
# box = [0] * N
# num_set = set()
# cnt, s = 0, 0
# nPr(0, len(alpha), N, s)
# print(cnt)