#!/usr/bin/env python
# coding: utf-8

# # 1)  write a python code which accepts a three or more digits number and prints :
#  
#  'A' if the last two digits of the number is divisible by 7. 
# 
#  'B' if the last two digits of number is divisible by 3.
# 
# 'AB' if the last two digits of the number is divisible by bothe 7 & 3.
# 
# 'Z' if last two digits of number is neither divisible by 7 nor 3.

# In[1]:


a=int(input('enter the number: ' ))
if a%7==0 :
   print(f'{a} is divisible by 7 and 3')
elif a%3==0:
    print(f'{a} is divisible by 3')
elif a%7==0 and a%3==0:
   print(f'{a} is divisible by 7 and 3')
else:
   print(f'{a} is not divisible by 7 and 3')

   


# In[3]:


num = (input('enter a three or greater than three digit positive integer'))

if len(num) >= 3 and (num.isdigit()):
    
    if (int(num[-2:]) % 3 == 0) and (int(num[-2:]) % 7 == 0):
        print('AB')
    elif (int(num[-2:]) % 3 == 0):
        print('B')
    elif (int(num[-2:]) % 7 == 0):
        print('A')
    else:
        print('Z')
        
else:
    print('Try entering a three digit or greater than three digit positive integer')


# ###### 2) write a code which accepts an alphabet from user and prints 'vowel' if the the alphabet is an vowel, 'not vowel' if the alphabet is not a vowel

# In[2]:


x=input('enter the alphabet: ' ).lower()
if len(x) == 1 and x.isalpha():
    
    if x in ['a','e','i','o','u']:
        print('vowel')
    else:
        print('not vowel')
        
else:
    print('enter a single alphabet')
    


# ##### 3) write a code to accepts four sides of an quadrilateral and print if it is a square or rectangle or an irregular quadrilateral.

# In[4]:


a = int(input('enter the length of side-1: '))
b = int(input('enter the length of side-2: '))
c = int(input('enter the length of side-3: '))
d = int(input('enter the length of side-4: '))

if a == b == c == d:
    print('square')
elif ((a == b) and (c == d)) or ((a == c) and (b == d)) or ((a == d) and (c == b)):
    print('rectangle')
else:
    print('irregular quad')


# 4) write a code to know weather it is vowel and number given is even/odd
# * vowel and even
# * vowel and odd
# * not vowel and even
# * not vowel and odd

# In[6]:


a = int(input('enter the number: '))
x = input('enter the string: ' ).lower()
if x in ['a','e','i','o','u'] and a%2==0:
    print(f'{x} is vowel and {a} is even' )
elif x in ['a','e','i','o','u'] and a%2!=0:
    print(f'{x} is  vowel and {a} is odd')
elif x not in ['a','e','i','o','u'] and a%2==0:
    print (f'{x} is not vowel and {a} is even')
elif x not in ['a','e','i','o','u'] and a%2!=0:
    print(f'{x} is not vowel and {a} is odd')
else:
    print('zz')


# In[ ]:




