"""
[같은 숫자는 싫어]
1. 이전과 같은 숫자가 나올 경우는 뒤에 동일값 전부 제거
2. 다른 값이 나오면 해당값을 담고 1번 다시 실행
cf. 담긴 값하고 동일한 값이 있더라도 이전값이 아니면 상관없음
"""

def solution(arr):
    answer = []
    start = arr[0]
    answer.append(start)
    for i in range(1,len(arr)):
        if arr[i] != start:
            start = arr[i]
            answer.append(start)
    return answer