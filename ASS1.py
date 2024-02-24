#!/usr/bin/env python
# coding: utf-8

# In[38]:


"""Write a Python program to store marks scored in subject “Fundamental of Data 
Structure” by N students in the class. Write functions to compute following:
 a)The average score of class
 b)Highest score and lowest score of class
 c)Count of students who were absent for the test
 d)Display mark with highest frequency"""


import array as arr
students=arr.array('i',())
n=int(input("Enter the no Students : "))
for i in range(n):
    marks=int(input("Enter the marks obtained in the FDS,[Enter -1 if student is absent]"))
    students.append(marks)
print(students)

def average ():
    sum1 = 0
    count = 0
    for i in range(n):
        if students[i] != -1:
            sum1 += students[i]
            count+= 1
    avg = sum1 / count
    print("Average of the class is", avg)
average()

def highest():
    max1=0
    for i in range(0, len(students)):
        if students[i]>max1:
            max1=students[i]
    print("Highest score of the class is ",max1)
highest()

def low():
    smallest = float('inf')
    for i in range(0, len(students)):
        if students[i] != -1:
            if students[i] < smallest:
                smallest = students[i]
    print("The smallest number is:", smallest)

low()
def count(arr):
    count1=0
    for i in range (0,len(arr)):
        if arr[i]==-1:
            count1+=1
    print(count1)
count(students)

def display_frequency():
    frequencies = {}
    for mark in students:
        if mark != -1:
            frequencies[mark] = frequencies.get(mark, 0) + 1

    max_frequency = max(frequencies.values())
    marks_with_max_frequency = []
    for mark, frequency in frequencies.items():
        if frequency == max_frequency:
            marks_with_max_frequency.append(mark)

    print("Marks with the highest frequency:", marks_with_max_frequency)


display_frequency()





