"""
[2016년]
실제 있는 날이라 datetime을 써도 될거 같지만,
윤년이라고 친절히 나와있으므로 그냥 품
"""

def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    end_day = {3:'SUN',4:'MON',5:'TUE',6:'WED',0:'THU',1:'FRI',2:'SAT'}
    today = sum(days[0:a-1]) + b
    day = today % 7
    answer = end_day[day]
    return answer