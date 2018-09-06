import math
##  Ques 1
list_1=[1,2,3]
a=[x**3 for x in list_1]
print(a)

##Ques 2
list_2=[x for x in range(1,15) if all(x%i!=0 for i in range(2,(int(x/2)+1)))]
print(list_2)

##Ques 3
'''A list comprehension '[]' executes immediately and returns a list
whereas a Generator expression '()' returns an object that can be iterated'''

##Lambda & Map
##Ques 1
Celsius = [39.2, 36.5, 37.3, 37.8]
a=list(map(lambda x:(9/5)*x+32,Celsius))
print(a)

##Ques 2

sq_num=(lambda x:x*x)
print(sq_num(5))

##Filter & Reduce
##Ques 1
n=int(input('Enter number of elements'))
p_list = []
l=[]
print('Enter the elements')
l=[int(input()) for i in range(0,n)]
def prime(x):
    flag=0
    for i in range(2,x):
        if(x % i == 0):
            return False
    if (flag == 0):
        return True
p_list= list(filter(prime, l))
print(p_list)

##Ques 2
from functools import *
n=int(input('Enter number of elements'))
mul_list = []
l=[]
print('Enter the elements')
l=[int(input()) for i in range(0,n)]
mul_list= reduce(lambda x,y : x*y, l)
print(mul_list)
