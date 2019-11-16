def solution(n):
    """
    [규칙] 이전의 값은 그 다음 가운데 값에 들어간다
    n=1 -> 1[0] -> 2[1]로 들어가고
    n=2 -> 2[0] -> 3[1], 2[1] -> 3[3], 2[2] -> 3[5]
    """
    papers = [[0], [0]]
    for pold in range(2, n+1):
        paper = [0] * (len(papers[pold-1])*2 +1) #n일 때의 함수의 길이
        value = 1
        for i in range(len(paper)):
            if i%2:
                paper[i] = papers[pold-1][i//2]
            else:
                if value == 0:
                    value = 1
                else:
                    value = 0
                paper[i] = value
        papers.append(paper)
    answer = papers[-1]
    return answer