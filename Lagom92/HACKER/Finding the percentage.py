# -*- coding: utf-8 -*- 
# Finding the percentage

"""
이름들과 점수들을 각각의 리스트로 만든다.
타겟이 이름들 리스트에서 몇 번째에 있는지 찾는다.
그 숫자에 3 을 곱하여 타겟의 점수가 점수들 리스트 어디에 있는지 찾는다.
찾은 점수들을 이용해 평균을 찾는다.

! 소수점 둘째자리까지 나와야 한다.
"""

N = int(input())
names = []
scores = []
target = ""

for _ in range(N):
    record = []
    record = input().split()
    names.append(record[0])
    scores.append(record[1])
    scores.append(record[2])
    scores.append(record[3])
target = input()

cnt = 0
for i in range(len(names)):
    if names[i] == target:
        cnt = i

cnt *= 3
res = (float(scores[cnt]) + float(scores[cnt+1]) + float(scores[cnt+2]))/3
print(format(res, '.2f'))