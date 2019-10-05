"""
1. 전화번호 길이에 따라 정렬
 -> 길이가 짧은거에서 큰 것만 비교해주면 되기에
2. 짧은 전화번호부터 시작하여 긴 전화번호에서 해당 길이만큼 같은게 있으면,
 Return False
 없다면, True
 -> 전화번호 비교에서는 슬라이싱도 되지만, in으로 처리해도 됨

이 풀이가 효율성을 통과한다는게 신기할 따름...

다른 사람 풀이 참조:
https://programmers.co.kr/learn/courses/30/lessons/42577/solution_groups?language=python3
"""

def solution(phone_book):
    phone_book.sort(key=len)
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return True