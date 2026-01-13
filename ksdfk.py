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


