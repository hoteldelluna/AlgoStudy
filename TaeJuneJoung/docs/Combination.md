# Combination

![Label](https://img.shields.io/badge/language-python-blue)

### nCr

```python
          n * n-1 *... *1
------------------------------------
(r*r-1...*1) * ((n-r)*(n-r-1)*...*1)
```



```python
"""
[조합]
N : 뽑을 숫자 길이
arr : 뽑을 수 있는 숫자들(데이터들)
box : 뽑은 값들을 담는 박스(리스트)
"""

def nCr(n, r):
    if r == 0:
        print(box)
    elif n < r:
        return
    else:
        box[r-1] = arr[n-1]
        nCr(n-1, r-1)
        nCr(n-1, r)

N = int(input())
arr = [i for i in range(1, 6)]
box = [0] * N
nCr(len(arr), N)
```

