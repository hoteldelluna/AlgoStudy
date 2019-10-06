"""
3, 5kg에서 가장 큰 것을 많이 가져갔을 때가 최소이니,
5kg을 기준으로 나눠보며 나눠지지 않으면 -3을 해주고 횟수 증가
N의 값이 음수가 나오면 딱 떨어지지 않으니 -1 출력
"""

N = int(input())
cnt = 0
while N > 0:
    if N % 5 == 0:
        cnt += N//5
        break
    else:
        N -= 3
        cnt += 1

if N < 0:
    cnt = -1
print(cnt)