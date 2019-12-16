"""
[달팽이는 올라가고 싶다]
낮 A 올라감
밤 B 내려감
막대 길이 V


while문 사용시 시간초과
- 참고해서 풀음
https://yahohococo.tistory.com/28
"""

A, B, V = map(int, input().split())

day = (V-B-1) // (A-B)
print(day+1)