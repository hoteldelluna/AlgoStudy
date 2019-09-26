"""
순열이면 1, 아니면 0

# 잘못 생각한 소스 -> anti_sum testcase의 경우를 고려하지 못함
# def solution(A):
#     return 1 if sum(range(len(A)+1)) == sum(A) else 0

생각해보니 숫자는 한번만 사용된다고 있어서, 중복이 없는 set이 만들어지기에
아래의 조건만으로 해결 가능
"""

def solution(A):
    return 1 if set(A) == set(range(1, len(A)+1)) else 0