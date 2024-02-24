#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Write a Python program to store first year percentage of students in array. Write 
function for sorting array of floating point numbers in ascending order using
 a) Selection Sort         b) Bubble sort and display top five scores."""



import array as arr

n=int(input("Enter the no of first year student :- "))
perofstudent=arr.array('d',())
for i in range(n):
    element=int(input("Enter the percentage of students :- "))
    perofstudent.append(element)

def Selection_sort(marks):
    for i in range(len(marks)):
        minx = i
        for j in range(i + 1, len(marks)):
            if marks[minx] > marks[j]:
                minx = j
        marks[i], marks[minx] = marks[minx], marks[i]
    print("Marks of students after performing Selection Sort on the list : ")
    for i in range(len(marks)):
        print(marks[i])
        

def Bubble_Sort(marks):
    n = len(marks)
    for i in range(n - 1):
        flag=0
        for j in range(0, n - i - 1):
            if marks[j] > marks[j + 1]:
                flag=1
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
                
        if (flag==0):
            break

    print("Marks of students after performing Bubble Sort on the list :")
    for i in range(len(marks)):
        print(marks[i])
    print("Top five scores after performing Bubble Sort:")
    for percentage in marks[-5:][::-1]:
        print(percentage)
        
while True:
    print("Choose a sorting function:")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        Selection_sort(perofstudent)
        break
    elif choice == 2:
        Bubble_Sort(perofstudent)
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")








# In[ ]:




