#day 8  { mini milestone python project- Random Password generator #simple version}

import random 

lower = "abdcddefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}*;/,._-"

all = lower+upper+symbols
length = 16
password = "".join(random.sample(all,length))
print(password)