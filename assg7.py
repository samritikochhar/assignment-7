#ques 1
a=eval(input('enter dictionary '))
b=int(input('enter the value '))
for k,v in a.items():
    if b==v:
        break
print(k)


#ques 2
a={'raman':{'maths':30,'physics':30,'chem':90},'Kapple':{'maths':90,'physics':50,'chem':10},'vipul':{'maths':78,'physics':30,'chem':60}}
b=str(input('enter name of student '))
for k,v in a.items():
    if b==k:
        print('maths=',a[k]['maths'])
        print('physics=',a[k]['physics'])
        print('chem=',a[k]['chem'])
    else:
        print("no data found")