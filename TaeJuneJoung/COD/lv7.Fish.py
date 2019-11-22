"""
상류(<-)/하류(->)라고 할 때,
두 경우가 만날 때는 하류(->) 상류(<-) 일때다.
이러한 경우가 발생할 때 큰 물고기가 작은 물고기를 먹고 본래의 방향으로 가면 된다. 
"""
def solution(A, B):
    box = [] #하류일때의 경우
    cnt = 0 #상류일때의 갯수
    for i in range(len(A)):
        if B[i] == 1:
            box.append(A[i])
        else:
            cnt += 1
            for j in range(len(box)-1, -1, -1):
                if box[j] > A[i]:
                    cnt -= 1
                    break
                else:
                    box.pop(-1)
    return cnt + len(box)