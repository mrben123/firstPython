from cgi import test
import turtle
import re
import json
import os

def main():
    a = 2
    print(': ',isinstance(a,int))

main()

class Staff:
    #所有员工的基类
    staffCount = 0

    def __init__(self, name, salary) -> None:
        pass
        self.name = name
        self.salary = salary
        Staff.staffCount += 1
    
    def displayCount(self):
        print ("Total staff  %d" % Staff.staffCount)

s = Staff("ben","3000")
s.displayCount()

def test():
    list1 = ['math','chemistry','physics']
    for  b in list1:                                                    
        #print('hi')
        if b == 'math':
            print('hello')
            continue
    pass


test()

def checkName():
    print( "卢嘉驹" in "我是卢嘉驹")

checkName()

str = 'this is string example'
print(str.startswith('t',2,4))
print(str.startswith('is',2,4))