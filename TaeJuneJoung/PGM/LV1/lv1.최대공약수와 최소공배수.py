def solution(n, m):
    def gcd(n, m):
        while n:
            n, m = m%n, n
        return m
    GCD = gcd(n, m)
    LCM = n * m / GCD
    return [GCD, LCM]