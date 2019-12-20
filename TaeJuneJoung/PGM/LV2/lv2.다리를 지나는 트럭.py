def solution(bridge_length, weight, truck_weights):
    time = 0
    # 앞에서부터의 pop은 n이 계속 앞당겨지기에...
    truck_weights = list(reversed(truck_weights))
    stack = []
    stack_time = []
    while truck_weights or stack:
        current = truck_weights[-1] if truck_weights else 0
        if sum(stack) + current <= weight:
            if current != 0:
                stack.append(truck_weights.pop())
                stack_time.append(0)
        
        for i in range(len(stack_time)):
            stack_time[i] += 1
        if stack_time[0] == bridge_length:
            stack.pop(0)
            stack_time.pop(0)
        
        time += 1

    answer = time + 1
    return answer