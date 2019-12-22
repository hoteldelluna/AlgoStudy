"""
[가장 큰 수]
다른 사람 소스를 보고 함
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))

"""
위의 소스를 이해하기 위한 활동
그러면 왜 x3인가? -> 범위가 1000까지이기에
"""
# a = ['666', '101010', '222', '111', '111111']
# b = ['6', '10', '2', '1', '11']
# a.sort()
# print(a)

# b.sort()
# print(b)