#types of inheritance

# single level
# multilevel
# multiple
# hierachical
# hybrid

# 1st example

class A:
    def m1(self):
        print("In m1")

class B:
    pass 
class C:
    pass

obj1 =A()
obj1.m1()

obj2 = B()
obj2.m1()


# 2nd example

#class A:
 #   def m1(self):
  #      print("In m1")

#class B(A):   #if we remove A then we will get attribute error   object 'B' has no attribute 'm1'
 #   pass

#obj1 =A()
#obj1.m1()

#obj2 =B()
#obj2.m1()

# 3rd example

#class A:
 #   def m2(self):
  #      print("In m1")

#class B(A):
 #   pass
#obj2 = B()
#obj2.m2()

# 4th example

#class A(object):
 #   def m1(self):
  #      print("In A-m1")

#class B(A):
 #   def m1(self):
  #      print("In B-m1")

#obj1 = A()        
#obj1.m1()

#obj2 = B()
#obj2.m1()

#5th example

#class A:
#    def m1(self):
#        print("In A-m1")

#class B(A):
#    def m1(self):
#        super().m1()

#obj2 = B()        
#obj2.m1()
    
#6th example

#class A(object):
#    def m1(self):
#        print("In A-m1")

#class B(A):
#    def m1(self):
#        print("In B-m1")
#        super().m1()

#obj2 = B()        
#obj2.m1()

# 7th example
#class A(object):
#    def m1(self):
#        print("In A-m1")

#class B(A): 
#    def m1(self):
#        print("In B-m1")
#    def call_par_m1(self):
#        super().m1

#obj1 = A()        
#obj1.m1()
#obj2. = B()
#obj2.call_par_m1()


#8th example
#class A (object):  #parent class/base class
#    def __ini__(self, a, b,c):
#        pass

#    def m1(self):
#        print("In A -m1")
#A(1 , 2, 3)   

#class B(A):  #child class/subclass/inherited class/derived class
#    def m1(self):
#        print("In B-m1")


#9th example

#class A:
#    def m1(self):
#        print("Inside A-m1")

#class B:   #class B(A):
#     def m1(self):
#        print("Inside B-m1")

#class C:   #class C(B)
#    def m1(self):
#        print("Inside C-m1")
 
#obj = C()
#obj.m1()

#10th example

class A:
    def m1(self):
        print("inside A-m1")

class B(A):
    def m1(self):
        print("Inside B-m1")

class C(B):
    def m1(self):
        print("inside C-m1")
#method resolution order  follow c3 linerization algorithm
#print(C.__mro__)    #tuple

print(C.mro())    #list
        


def func():
    print("for testing git")



     








