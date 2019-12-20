def solution(n, arr1, arr2):
    answer = [0] * n
    for i in range(n):
        num = (bin(arr1[i] | arr2[i]))[2:]
        num = f'{num:0>{n}}'
        answer[i] = '#' if int(num[0]) else ' '

        for j in range(1, len(num)):
            if num[j] == '1':
                answer[i] += '#'
            else:
                answer[i] += ' '

    return answer

    """
    다른사람 풀이
    """
    def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer