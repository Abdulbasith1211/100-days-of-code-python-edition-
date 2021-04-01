#DAY 10 CODE

"""each problem link and its solution are given"""


#Problem   : https://www.hackerrank.com/challenges/py-if-else/problem
#!/bin/python3

import sys

n = int(input())
if n%2==1 or n in range (5,21):
    print("Weird")
else:
    print("Not Weird")

    


#Problem   : https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


#Problem   : https://www.hackerrank.com/challenges/python-division/problem

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)   

#Problem   : https://www.hackerrank.com/challenges/python-loops/problem

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)



#Problem   : https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False    
    leap = (year%400==0) or (year%4==0 and year%100!=0)    
    return leap

year = int(input())
print(is_leap(year))




#Problem   : https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    ar=range(1,n+1)
    for i in ar:
        print(i,end="")








#Problem   : https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
        name, *line = input().split()
    for _ in range(n):
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    res = sum(student_marks[query_name])/len(student_marks[name])
    print("{:.2f}".format(res))


#Problem   : https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ar = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    print(ar)

#Problem   : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr), reverse=True)[1])



#Problem   : https://www.hackerrank.com/challenges/python-lists/problem


if __name__ == '__main__':
    N = int(input())
    ar = []
    for i in range(0, N):
        tmp_str = input()
        tmp_str_ar = tmp_str.strip().split(" ")
        cmd = tmp_str_ar[0]
        if cmd == "print":
            print(ar)
        elif cmd == "sort":
            ar.sort()
        elif cmd == "reverse":
            ar.reverse()
        elif cmd == "pop":
            ar.pop()
        elif cmd == "count":
            val = int(tmp_str_ar[1])
            ar.count(val)
        elif cmd == "index":
            val = int(tmp_str_ar[1])
            ar.index(val)
        elif cmd == "remove":
            val = int(tmp_str_ar[1])
            ar.remove(val)
        elif cmd == "append":
            val = int(tmp_str_ar[1])
            ar.append(val)
        elif cmd == "insert":
            pos = int(tmp_str_ar[1])
            val = int(tmp_str_ar[2])
            ar.insert(pos, val)



#Problem   : https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)
        scores.append(score)
    second_min_score = sorted(set(scores))[1]
    filtered_student_names = sorted([student[0] for student in students if student[1] == second_min_score])
    print("\n".join(filtered_student_names))


# Problem   : https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))



#Problem   : https://www.hackerrank.com/challenges/python-print/problem


if __name__ == '__main__':
    n = int(input())
    ar=range(1,n+1)
    for i in ar:
        print(i,end="")


#Problem   : https://www.hackerrank.com/challenges/swap-case/problem



def swap_case(sentence):
    updated_s = ""
    for c in sentence:
        if c.isupper():
            updated_s += c.lower()
        elif c.islower():
            updated_s += c.upper()
        else:
            updated_s += c
    return updated_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



#Problem   : https://www.hackerrank.com/challenges/python-string-split-and-join/problem
def split_and_join(sentence):
    return "-".join(sentence.split())


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)




#Problem   : https://www.hackerrank.com/challenges/whats-your-name/problem



def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


#Problem   : https://www.hackerrank.com/challenges/python-mutations/problem



def mutate_string(string, position, character):
    chars = list(string)
    chars[position] = character
    return "".join(chars)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)



#Problem   : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

n = input()
ar = map(int,input().split(' '))
ar=set(ar)
print(sum(ar) / len(ar))





#Problem   : https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
set_a = set(map(int, input().split()))
n = int(input())
set_b = set(map(int, input().split()))
set_a_diff = set_a.difference(set_b)
set_b_diff = set_b.difference(set_a)
for i in sorted(set_a_diff.union(set_b_diff)):
    print(i)




#Problem   : https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    flag_alnum = False
    flag_alpha = False
    flag_digit = False
    flag_lower = False
    flag_upper = False
    for i in s:
        if i.isalnum():
            flag_alnum = True
        if i.isalpha():
            flag_alpha = True
        if i.isdigit():
            flag_digit = True
        if i.islower():
            flag_lower = True
        if i.isupper():
            flag_upper = True

    print(flag_alnum)
    print(flag_alpha)
    print(flag_digit)
    print(flag_lower)
    print(flag_upper)



