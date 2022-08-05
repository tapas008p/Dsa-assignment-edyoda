#!/usr/bin/env python
# coding: utf-8

# # Question 1

#  Write a program to find all pairs of an integer array whose sum is equal to a given number 

# In[78]:


def Q1(array,target):
    return [(array[i],array[j]) for i in range(len(array)) for j in range(len(array)) if array[i]+array[j]==target and i!=j]


# In[79]:


array=[10,20,14,16,12,15]
Q1(array,30)


# # Question 2

# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array

# In[80]:


def Q2(array):
    return array[::-1]


# In[81]:


Q2([10,30,50,60,40])


# # Question 3

# Q3. Write a program to check if two strings are a rotation of each other?

# In[98]:


def Q3(string1,string2):
    if len(string1)==len(string2):
        new=string1+string1
        if string2 in new:
            return "Two strings are rotation of each other"
        else:
            return "Two strings are not rotation of each other"
    else:
        return "Two strings are not rotation of each other"


# In[100]:


Q3("aacd","acda")


# # Question 4

# Q4. Write a program to print the first non-repeated character from a string?

# In[101]:


def Q4(string):
    for i in string:
        if string.count(i)==1:
            break
    return i


# In[102]:


Q4("abbccd")


# # Question 5

# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it

# Tower of Hanoi :
# ________________
# 
#    Tower of Hanoi, is a mathematical puzzle which consists of three towers(source tower,destination tower,auxiliary tower) and more than one rings.These rings are of different sizes and stacked upon in an ascending order.
# 
#  Objective : The objective  is to move all the disks to destination tour from the source tour without violating the sequence of arrangement.
#  
#  Rules:
#  1. Only one disk can be moved among the towers at any given time.
#  2. Only the "top" disk can be removed.
#  3. Large disk can't sit over a small disk.
#  
#  Tower of Hanoi puzzle with n disks can be solved in minimum $(2^n−1)$ steps.
# 

# In[92]:


def Q5_Tower_Of_Hanoi(n,source,destination,auxiliary):
    if n==1:
        print("Disk 1",source,"--->",destination)
        return
    Q5_Tower_Of_Hanoi(n-1,source,auxiliary,destination)
    print("Disk",n,source,"--->",destination)
    Q5_Tower_Of_Hanoi(n-1,auxiliary,destination,source)


# In[93]:


Q5_Tower_Of_Hanoi(4,'A','B','C')


# # Question 6

# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression

# In[94]:


def isOperator(x):
    l=["+","-","*","/"]
    if x in l:
        return True
    else:
        return False
    
def post_pre(expression):
    s=[]
    for i in range(len(expression)):
        if isOperator(expression[i]):
            operand1=s.pop(-1)
            operand2=s.pop(-1)
            s.append(expression[i]+operand2+operand1)
        else:

            s.append(expression[i])
    return ''.join(s)
  
post_pre("ABC/-AK/L-*")


# # Question 7

# Q7. Write a program to convert prefix expression to infix expression.

# In[95]:


def isOperator(x):
    l=["+","-","*","/"]
    if x in l:
        return True
    else:
        return False
    
def pre_in(expression):
    expression=expression[::-1]
    s=[]
    for i in range(len(expression)):
        if isOperator(expression[i]):
            operand1=s.pop(-1)
            operand2=s.pop(-1)
            s.append("("+operand1+expression[i]+operand2+")")
        else:

            s.append(expression[i])
    return ''.join(s)
  
pre_in("*-A/BC-/AKL")


# # Question 8

# Q8. Write a program to check if all the brackets are closed in a given code snippet.

# In[96]:


def all_bracket_closed(expression):
    opening_brackets=['{','[','(']
    s=[]
    for i in range(len(expression)):
        if expression[i] in opening_brackets:
            s.append(expression[i])
        elif len(s)!=0 and s[-1]=='[' and expression[i]==']':
            s.pop()
        elif len(s)!=0 and s[-1]=='(' and expression[i]==')':
            s.pop()
        elif len(s)!=0 and s[-1]=='{' and expression[i]=='}':
            s.pop()
        else:
            return 'all the brackets are not closed'
    if len(s)==0:
        return 'all the brackets are closed'
    else:
        return 'all the brackets are not closed'
        
    
all_bracket_closed("[(])")


# In[97]:


'''def all_bracket_closed(expression):
    expression=expression.replace('()','')
    expression=expression.replace('[]','')
    expression=expression.replace('{}','')
    if len(expression)==0:
        return 'all the brackets are closed'
    else:
        return 'all the brackets are not closed'
    
all_bracket_closed("[(])")'''


# # Question 9

# Q9. Write a program to reverse a stack.

# In[108]:


class Stack:
    
    def __init__(self):
        self.data=[]
        
    def push(self,element):
        self.data.append(element)
        return
    
    def pop(self):
        if len(self.data)==0:
            return "stack is empty"
        self.data.pop(-1)
        return
        
    def printl(self):
        return self.data
    
    def reverse(self):
        return self.data[::-1]

        
        
s=Stack()
s.push("15")
s.push("20")
s.push("13")
s.push("18")
s.push("11")
print("Original stack",s.printl())
print("Reversed stack",s.reverse())


# # Question 10

# Q10. Write a program to find the smallest number using a stack.

# In[109]:


class Stack:
    
    def __init__(self):
        self.data=[]
        
    def push(self,element):
        self.data.append(element)
        return
    
    def pop(self):
        if len(self.data)==0:
            return "stack is empty"
        self.data.pop(-1)
        return
        
    def printl(self):
        return self.data
    
    def find_smallest_number(self):
        s=sorted(self.data)
        return s[0]
        
        
s=Stack()
s.push("15")
s.push("20")
s.push("13")
s.push("18")
s.push("11")
print("Original stack",s.printl())
print("smallest number of the stack is",s.find_smallest_number())


# In[112]:





# In[ ]:




