N, K = map(int, input().split())

kind_list = []
for _ in range(N):
    _kind_money = int(input())
    if (_kind_money <= K):
        kind_list.append(_kind_money)

cnt = 0

for idx in range(len(kind_list)-1, -1, -1):
    _kind_cnt = K // kind_list[idx]
    cnt += _kind_cnt
    K %= kind_list[idx]

print(cnt)