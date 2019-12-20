def solution(N, stages):
    answer = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            cnt = stages.count(stage)
            answer[stage] = cnt / denominator
            denominator -= cnt
        else:
            answer[stage] = 0
    return sorted(answer, key=lambda i: answer[i], reverse=True)