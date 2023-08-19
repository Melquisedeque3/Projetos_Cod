import math
import os
import random
import re
import sys

n = int(input().strip())
p = n % 2 == 0
i = n % 2 != 0

# print (p)
# print (i)

if n > 2 and n < 5 and n % 2 == 0:
# elif 
    print ('Not Weird p')
elif n > 6 and n < 20 and n % 2 == 0:
    print('Weird')
elif n > 20 and p == True:
    print('Not Wierd 1')
else:
    print ('Weird i')