# 부분집합

---



## 부분집합 출력

```python
def sub_set():
    for i in range(1, 1 << M):
        for j in range(M):
            if i & (1 << j) != 0:
                print(set_box[j], end=" ")
        print()

#example
set_box = [1,2,3,4]
M = len(set_box)
sub_set()
```



## 부분집합의 합

```python
def sum_sub_set():
    for i in range(1, 1 << M):
        s = 0
        for j in range(M):
            if i & (i << j) != 0:
                s += set_box[j]
        print(s)

#example
set_box = [1,2,3,4]
M = len(set_box)
sum_sub_set()
```

