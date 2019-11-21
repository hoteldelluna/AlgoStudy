# Codility 
# Lesson 7 Fish

'''
0: upstream
1: downstream

다른사람의 아이디어로 풀이함

B 중 1이 나오면 box에 넣는다
0이 나올때 box에 숫자가 있다면 비교

주의! box에 수만큼 물고기가 만나서 싸워야함!

'''

def solution(A, B):
    box = list()        # down인것만 모으는 곳
    N = len(A)
    cnt = 0
    
    for i in range(N):
        if B[i] == 1:
            box.append(A[i])
        else:
            cnt += 1
            if box:
                for j in range(len(box)-1, -1, -1):
                    if box[j] > A[i]:
                        cnt -= 1
                        break
                    else:
                        box.pop(len(box)-1)
       
    return cnt + len(box)

a = [4, 3, 2, 1, 5]
b = [0, 1, 0, 0, 0]
res = solution(a, b)
print(res)