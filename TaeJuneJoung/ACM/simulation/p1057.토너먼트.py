"""
[시뮬레이션]
토너먼트에서 부전승은 고려하지 않고
2개의 짝이 이뤄질 때의 관계를 보면 된다.
홀수일 때는 해당 수의 +1이 대결상대며,
짝수일 때는 해당 수의 -1이 대결상대이다.

토너먼트 다음단계에 가서는
짝수는 나누기 2의 값의 순서를 가지고,
홀수는 나누기 2를 한 후 +1의 순서를 가진다.
"""

N, A, B = map(int, input().split())
cnt = 0
while A > 0:
    cnt += 1
    if A%2:
        if A+1 == B:
            break
        else:
            A = A//2 +1
            if B%2:
                B = B//2 +1
            else:
                B = B//2
    else:
        if A-1 == B:
            break
        else:
            A = A//2
            if B%2:
                B = B//2 +1
            else:
                B = B//2
print(cnt)