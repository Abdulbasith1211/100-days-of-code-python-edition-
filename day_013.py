#DAY 13  - [ Array - problem solving ]


#Problem : https://www.hackerrank.com/challenges/2d-array/problem

import sys


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

    
best = 0
for ind_i in range(6-2):
    for ind_j in range(6-2):
        temp = 0
        temp += arr[ind_i][ind_j] + arr[ind_i][ind_j+1] + arr[ind_i][ind_j+2]
        temp += arr[ind_i+1][ind_j+1]
        temp += arr[ind_i+2][ind_j] + arr[ind_i+2][ind_j+1] + arr[ind_i+2][ind_j+2]
        if ind_i == 0 and ind_j == 0:
            best = temp
        else:
            best = max(best, temp)
    
print(best)




#Problem   :  https://www.hackerrank.com/challenges/arrays-ds/problem

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(" ".join(map(str, arr[::-1])))





#Problem: https://www.hackerrank.com/challenges/dynamic-array/problem




if __name__ == "__main__":
    N, Q = map(int, input().strip().split(' '))
    sequences = [[] for _ in range(N)]
    last_answer = 0
    
    for q in range(Q):
        q_type, x, y = map(int, input().strip().split(' '))
        seq_num = (x ^ last_answer) % N
        
        if q_type == 2:
            last_answer = sequences[seq_num][y % len(sequences[seq_num])]
            print(last_answer)
        else:
            sequences[seq_num].append(y)





#Problem : https://www.hackerrank.com/challenges/array-left-rotation/problem


import sys

def leftRotation(a, d):
    out = list(a)
    a_len = len(a)
    for ind, el in enumerate(a):
        out[(ind + a_len - d) % a_len] = el

    return out
        
if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))




#Problem : https://www.hackerrank.com/challenges/sparse-arrays/problem


if __name__ == "__main__":
    strings = []
    N = int(input().strip())
    for _ in range(N):
        strings.append(input().strip())
        
    Q = int(input().strip())
    for _ in range(Q):
        substr = input().strip()
        print(strings.count(substr))





#Problem : https://www.hackerrank.com/challenges/crush/problem


import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    array = [0] * (n+1)
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        
        array[a-1] += k
        if b+1 <= n:
            array[b] -= k
        
    res_max = 0
    res = 0
    for dif in array:
        res += dif
        res_max = max(res_max, res)
        
    print(res_max)
        