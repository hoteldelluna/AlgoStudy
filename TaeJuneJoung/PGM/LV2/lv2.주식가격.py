def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        cnt = 0
        isOnce = False
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                isOnce = True
                break
            else:
                answer[i] += 1
        if isOnce:
            answer[i] += 1
    return answer