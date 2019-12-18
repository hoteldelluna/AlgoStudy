"""
[문자열 내림차순으로 배치하기]
문자열은 sort가 되지 않는다. -> Immutable하기 때문에
그러면 다른 변수에 적용시키는 sorted를 활용하자
sorted는 정렬 후에 문자열을 리스트로 반환시켰다.
답을 만들기 위해 join사용
"""

def solution(s):
    answer = sorted(s, reverse=True)
    return ''.join(answer)