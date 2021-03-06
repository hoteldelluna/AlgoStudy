"""
bin을 사용하여 Binary형태로 바꿔준다.
바뀌면서 type이 'str'이 된다는 것을 주의해야한다.
'0b'의 값도 붙어서 나오니 2번 index부터 시작
"""

def solution(N):
    N = bin(N)[2:]
    base_idx, maxV = 0, 0
    for idx, num in enumerate(N):
        if num == '1':
            base_idx = idx - base_idx -1
            maxV = base_idx if base_idx > maxV else maxV
            base_idx = idx
    return maxV

"""
다른 방법]
def result(N):
	return max(map(len, str(bin(N))[2:].strip('0').strip('1').split('1')))
"""