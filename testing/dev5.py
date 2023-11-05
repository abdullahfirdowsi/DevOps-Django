def fibonacci_series(n):
    a=0
    b=1
    output=[]
    for i in range(n):
        c=a+b
        output.append(c)
        a=b
        b=c
    return output
a=fibonacci_series(5)
print(a)

def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
b=fact(5)
print(b)

def are_anagrams(a,b):
    if sorted(a)==sorted(b):
        print("It is anagram")
        return True
    else:
        print("not anagram")
are_anagrams("saran","naras")

def is_pali(s):
    if s==s[::-1]:
        print("It is a palindrome")
    else:
        print("not a palindorme")
is_pali('121')

class Circle:
    def __init__(self,radius):
        self.radius=radius
        self.pi=3.14
    def area(self):
        return self.pi*self.radius**2
    def circumference(self):
        return 2*self.pi*self.radius
c=Circle(radius=345)
print(c.area())
print(c.circumference())

class BankAccount:
    def __init__(self,ib):
        self.ib=ib
    def deposit(self,amount):
        self.ib+=amount
    def withdraw(self,amount):
        if self.ib>amount:
            self.ib-=amount
            return True
        else:
            return False
    def get_balance(self):
        return self.ib
d=BankAccount(ib=30)
d.deposit(20)
print(d.withdraw(10))
print(d.get_balance())

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.course=[]
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def enroll_course(self,courses):
        self.course+=[courses]
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_courses(self):
        return self.course
e=Student("Arun",22)
e.set_name("Kumar")
e.enroll_course("CSE")
e.enroll_course("IT")
print(*e.get_courses())
print(e.get_name())

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if self.is_empty():
            print("the stack is underflow")
        else:
            return self.stack.pop()
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
s=Stack()
s.push(4)
s.push(5)
s.push(6)
print(s.pop())
print(s.size())

class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if self.is_empty():
            print("The Queue is empty")
        else:
            return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue)==0
q=queue()
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
print(q.is_empty())

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.salary=1000
    def set_name(self,name):
        self.name=name
    def set_id(self,id):
        self.id=id
    def set_salary(self,salary):
        self.salary=salary
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_salary(self):
        return self.salary
a=Employee("Arun",10)
a.set_name("kumar")
a.set_id(20)
a.set_salary(3000)
print(a.get_name())
print(a.get_id())
print(a.get_salary())

import unittest
class testArun(unittest.TestCase):
    def test1(self):
        f=fibonacci_series(5)
        self.assertEqual(f,[1,2,3,5,8])
    def test2(self):
        a=fact(5)
        self.assertTrue(a,120)
    def test3(self):
        a=are_anagrams("saran","naras")
        self.assertTrue(a)
    def test4(self):
        c=Circle(radius=345)
        self.assertEqual(c.area(),373738.5)
unittest.main()
