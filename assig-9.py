# ques 1
a=3
try:
    if a<4:
        a=a/(a-3)
except ZeroDivisionError:
    print("this question has Zero division error")
    print(a)
#ques 2
l=[1,2,3]
try:
    print(l[3])
except IndexError:
     print("It shows index error\n")
     print (l)
# ques 3
"""
OUTPUT = An Exception
NameError: Hi there
"""
# ques 4
"""
-5.0
a/b result in 0
"""
#ques 5
try:
    a=int(input())
    print(a)
except ValueError:
     print("Enter desired input")

l=[1,2,3]
try:
  print(l[3])
except IndexError:
  print("It shows index error\n")
  print (l)
try:
    import abcdef
except ImportError as msg:
    print(msg)