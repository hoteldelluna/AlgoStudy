# SW Expert 5648. [모의 SW 역량테스트] 원자 소멸 시뮬레이션

'''
1000번을 이동하면 만날 것들은 다 만나고 못 만나는 것들은 계속 못만날 것 이므로
1000번 이동시켜서 같은게 있는지 확인하는 방식으로 했음
-ing
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0

def f(arr,k,  s):
    for i in range(4000):
        for j in range(k):
            if arr[j][2] == 0:
                arr[j][1] += 0.5
            elif arr[j][2] == 1:
                arr[j][1] -= 0.5
            elif arr[j][2] == 2:
                arr[j][0] -= 0.5
            else:
                arr[j][0] += 0.5

            if arr[j][0] > 1000 or arr[j][0] < -1000 or arr[j][1] > 1000 or arr[j][1] < -1000:
                arr[j].pop()
                k -= 1

        for m in range(N):
            for n in range(N):
                if m != n:
                    if arr[m][0] == arr[n][0] and arr[m][1] == arr[n][1]:
                        res += arr[m][3]
                        break




    print("#{} {}".format(tc, res))