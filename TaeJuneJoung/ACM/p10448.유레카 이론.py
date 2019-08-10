"""
[완전탐색]
시간이 중요한 문제
완전탐색에 기본적인 부분들을 만들어놓고
테스트 케이스 때 저장된 값을 비교하여 시간단축

중복조합을 이용한 문제
조합을 짜는 소스를 함수를 이용해서 하면 더 활용적임

순열과 조합의 개념 참고사이트
: https://m.blog.naver.com/PostView.nhn?blogId=alwaysneoi&logNo=100155625557&proxyReferer=https%3A%2F%2Fwww.google.com%2F
"""

K = 1000
N = int((2*K)**(0.5))
nums = [0] * (N+1)
for i in range(1, N+1):
    nums[i] = i*(i+1)//2

V = []
for i in range(1, N+1):
    for j in range(i, N+1):
        for k in range(j, N+1):
            sum_num = nums[i] + nums[j] + nums[k]
            V.append(sum_num)

T = int(input())
for t in range(T):
	K = int(input())
	if K in set(V):
		print(1)
	else:
		print(0)