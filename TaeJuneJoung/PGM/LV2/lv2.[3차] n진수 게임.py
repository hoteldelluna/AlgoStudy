"""
[[3차]n진수 게임]
다른 사람 소스를 참고하여 해결함
"""

def n_base(numbers, N):
    table = []
    n_number = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    if numbers == 0:
        return '0'
    while numbers:
        table.append(str(n_number[numbers % N]))
        numbers //= N
    return ''.join(list(reversed(table)))

def solution(n, t, m, p):
    answer = ''
    numbers = [n_base(i, n) for i in range(t*m)]
    numbers = ''.join(numbers)
    answer = [numbers[(p-1)+i*m] for i in range(0, t)]
    return ''.join(answer)

"""
다른 방법
"""

# 1번
big = ["A","B","C","D","E","F"]
def solution(n, t, m, p):
    a="0"
    i=0
    #for i in range(t*m):
    while True:
        if len(a)>=t*m:
            break
        b=""
        j=i
        while (j):
            if j%n>9:
                b=big[j%n-10]+b
            else:
                b=str(j%n)+b
            j=j//n
        a=a+b
        i=i+1
    answer = a[p-1::m][:t]
    return answer

# 2번
def solution(n, t, m, p):
    data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    numbers = "0"
    for number in range(1, t*m):
        temp = []
        while number > 0:
            temp.append(data[number%n])
            number //= n
        numbers += "".join(reversed(temp))

    return numbers[p-1:t*m:m]