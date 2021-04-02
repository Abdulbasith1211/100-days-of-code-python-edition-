#DAY 11 

#Problem   : https://www.hackerrank.com/challenges/text-alignment/problem


thickness = int(input())
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
        thickness * 6))





#Problem   : https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)



#Problem   : https://www.hackerrank.com/challenges/python-string-formatting/problem

n = int(input().strip())
w = len(str(bin(n))[2:])
for i in range(1,n+1,1):
    o = str(oct(i))[2:]
    h = str(hex(i))[2:]
    h = h.upper()
    b = str(bin(i))[2:]
    d = str(i)
    print('{:>{width}} {:>{width}} {:>{width}} {:>{width}}'.format(d,o,h,b,width=w))



#Problem   : https://www.hackerrank.com/challenges/designer-door-mat/problem

N, M = map(int, input().split())
for i in range(1, N, 2):
    print(int((M - 3 * i) / 2) * '-' + (i * '.|.') + int((M - 3 * i) / 2) * '-')
print(int((M - 7) / 2) * '-' + 'WELCOME' + int((M - 7) / 2) * '-')
for i in range(N - 2, -1, -2):
    print(int((M - 3 * i) / 2) * '-' + (i * '.|.') + int((M - 3 * i) / 2) * '-')


    
#Problem   : https://www.hackerrank.com/challenges/capitalize/problem

s = input()
s_ar = s.split(' ')
final_ar = []
space = ' '
for w in s_ar:
    final_ar.append(w.capitalize())
print(space.join(final_ar))



#Problem   : https://www.hackerrank.com/challenges/the-minion-game/problem

s = input().strip()
s_length = len(s)
vowel_list = ['A','E','I','O','U']
stuart_point = 0
kevin_point = 0
for i in range(s_length):
    if s[i] in vowel_list:
        kevin_point += s_length - i
    else:
        stuart_point += s_length - i
if stuart_point == kevin_point:
    print('Draw')
elif kevin_point > stuart_point:
    print('Kevin',kevin_point)
else:
    print('Stuart',stuart_point)



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


#Problem   : https://www.hackerrank.com/challenges/calendar-module/problem

import datetime
import calendar
m,d,y=map(int,input().split())
input_date = datetime.date(y,m,d)
print(calendar.day_name[input_date.weekday()].upper())



#Problem   : https://www.hackerrank.com/challenges/collections-counter/problem

x = int(input())
shoe_size = list(map(int,input().split()))
n = int(input())
sell = 0
for i in range(n):
    s, p = map(int,input().split())
    if s in shoe_size:
        sell = sell + p
        shoe_size.remove(s)
print(sell)




#Problem   : https://www.hackerrank.com/challenges/zipped/problem

n, x = map(int,input().split())
ar = [0 for i in range(n)]
for i in range(x):
    temp_ar=list(map(float,input().split()))
    for j in range(n):
        ar[j] += temp_ar[j]
for i in range(n):
    print(ar[i]/x)


#Problem   : https://www.hackerrank.com/challenges/input/problem

x,k=list(map(int,raw_input().split()))
print(input() == k)



#Problem   : https://www.hackerrank.com/challenges/python-sort-sort/problem

n, m = map(int,input().split())
ar = []
for i in range(n):
    ar.append(list(map(int,input().split())))
k = int(input())
ar = sorted(ar,key = lambda x:x[k])
for i in ar:
    [print(x,end=' ') for x in i]
    print('')




#Problem   : https://www.hackerrank.com/challenges/polar-coordinates/problem

import cmath
z = complex(input())
p = cmath.polar(z)
print(p[0])
print(p[1])
