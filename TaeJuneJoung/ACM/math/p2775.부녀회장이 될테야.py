"""
[부녀회장이 될테야]
1 <= k <= 14
1 <= n <= 14
"""

apart = [[i for i in range(1, 15)] for i in range(15)]

for i in range(1, 15): #층수
    for j in range(1, 14): #호수
        apart[i][j] = sum(apart[i-1][:j+1])

for t in range(int(input())):
    k = int(input())
    n = int(input())
    print(apart[k][n-1])