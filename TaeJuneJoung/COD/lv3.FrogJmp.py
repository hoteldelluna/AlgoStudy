"""
divmod를 사용하는게 숫자가 크다면 조금 더 빠르다
숫자가 작은 경우네는 오히려 아래와 같이 하는 경우가 빠르다
"""

def solution(X, Y, D):
    return (Y-X)//D +1 if (Y-X)%D else (Y-X)//D