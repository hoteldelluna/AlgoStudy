# codility FrogJmp
# lesson 3
'''
개구리가 X에서 Y로 이동 하고자 할때 
개구리는 D만큼 점프가 가능하다.

그냥 나눠주고 목적지 Y를 넘어가면 1을 더해줬다.
'''

def solution(X, Y, D):
    a, b = divmod(Y-X, D)
    return a+1 if b>0 else a