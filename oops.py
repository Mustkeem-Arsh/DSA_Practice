class dog:
    def bark(self):
        print("Dog barks")
    
class cat:
    def meow(self):
        print("Cat meows")

class animal(dog, cat):
    def spaek(self):
        print("This class will have different animal methods")

# d = dog()
# d.bark()
# c = cat()
# c.meow()

a = animal()
a.spaek()
a.bark()
a.meow()


class bird():
    pass

class surr():
    pass

# Single heritance
# multiple inheritance
# multi level inheritance
# Heirarichal inheritance
# hybrid inheritance

# single 
class parent:
    pass
class child(parent):
    pass

# Multiple
class dog:
    def bark(self):
        print("Dog barks")
    
class cat:
    def meow(self):
        print("Cat meows")

class animal(dog, cat):
    def spaek(self):
        print("This class will have different animal methods")

# multi level

class A:
    pass
class B(A):
    pass
class C(B):
    pass

# hierarchical 

class A:
    pass

class a1(A):
    pass
class a2(A):
    pass

# hybrid
class A:
    pass
class B(A):
    pass
class C (A):
    pass
class D(B,C):
    pass



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
