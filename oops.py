'''
create database of students using class and object. 
required things : 
name, roll
'''

class db:
    def __init__(self,name):
        self.a = name
    def roll_no(self, b):
        self.b = b
    def display(self):
        print(f'the name is {self.a} and roll number is {self.b}')

s1 = db("Zion")
# s1.name("Zion")
s1.roll_no(10)

# s2 = db()
# s2.name("lily")
# s2.roll_no(11)
# # s2.display()

# s3 = db()
# s3.name("adam")
# s3.roll_no(12)


s1.display()

'''
constructor
'''
