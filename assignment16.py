#Q.1- Write a python script to create a databse of students named Students.
import pymongo
client=pymongo.MongoClient()
'''initiallising monghgfoclient'''
database = client['Students']
'''connecting to students'''
student_table= database['Students']




'''#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
for i in range(1,11):
        
        b=input('enter name')
        c=int(input('enter subject marks'))
        if c<=100:
            student_table.insert_one({'Name':b,' Marks':c})
        else:
            print('enter valid marks')'''

#Q.4- Print the names of all the students who scored more than 80 marks.
data=student_table.find({"Marks":{"$gt":80}})
for d in data:
        print(d)