#Q1
f=open('e.txt','r')
a=f.read()
print(a)
f.close()

#Q2
f=open('e.txt','r')
a=f.read()
g=a.count('s')
print('The count of is : ',g)

#Q3
f=open('e.txt','r')
a=f.read()
q=open('q.txt','a+')
q.write(a)
q.seek(0)
n=q.read()
print(n)
f.close()
q.close()

#Q4
f=open('e.txt')
g=open('q.txt')
j=open('w.txt','w+')
h=f.readlines()
l=g.readlines()
for i,q in zip(h,l):
    j.write(str(i))
    j.write(str(q))
j.seek(0)
y=j.read()
print(y)

#Q5
f=open('e.txt')
t=open('file.txt','w+')
h=f.readlines()
h.sort()
t.write(str(h))
t.seek(0)
o=t.read()
print(o)
