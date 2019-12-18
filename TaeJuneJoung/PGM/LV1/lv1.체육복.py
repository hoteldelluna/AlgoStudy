"""
[체육복]
프로그래머스 lv1문제에서 카카오 문제를 제외하고는
이 문제가 가장 어렵지 않을까 싶다.

집합을 이용해서 푸는 도중에
`minus = (set_reserve & set_lost)`를 이렇게 변수화하지 않고
값으로 하였다가 봉변...
"""

def solution(n, lost, reserve):
    set_lost = set(lost)
    have_person = set(map(int, range(1, n+1))) - set_lost
    set_reserve = set(reserve)
    minus = (set_reserve & set_lost)
    have_person = have_person | minus
    set_lost = set_lost - minus
    set_reserve = set_reserve - minus
    for i in list(set_reserve):
            
        if i-1 in set_lost and i-1 not in have_person:
            have_person = have_person | set([i-1])
            set_lost -= set([i-1])
            
        elif i+1 in set_lost and i+1 not in have_person:
            have_person = have_person | set([i+1])
            set_lost -= set([i+1])
    return len(have_person)