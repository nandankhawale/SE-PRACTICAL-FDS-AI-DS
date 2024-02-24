#!/usr/bin/env python
# coding: utf-8

# In[8]:


""" Write a Python program to compute following operations on String:
 a)To display word with the longest length
 b)To determines the frequency of occurrence of particular character in the string
 c)To check whether given string is palindrome or not
 d)To display index of first appearance of the substring
 e)To count the occurrences of each word in a given string"""

stringg=input("Enter the string : ")
splited=stringg.split()
def longestleng(string):
    longest_word = None
    max_length = len(string[0])
    for i in string:
         if len(i) > max_length:
            max_length = len(i)
            longest_word = i

    print("the longest word is : ",longest_word)
longestleng(splited)
target=input("Enter the charcter to determine the frequency : ")

def frequency(string, target):
    character_count = 0
    for char in string:
         if char == target:
            character_count += 1
    print("Count of the  targeted string is",character_count)
frequency(stringg,target)

word=input("enter the word to check the palindrome : ")
def palindrome(word):
    if word==word[::-1]:
        print("IT is palindrome")
    else:
        print("It is not palindrome")
palindrome(word)

def find_substring_index(text, substring):
    index = text.find(substring)
    return index
substring = input("Enter the substring to find: ")
print(find_substring_index(stringg, substring))

def count_word_occurrences(text):
    word_counts = {}

    for word in text:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    for word, count in word_counts.items():
        print(f"'{word}' occurs {count} time(s) in the text.")

   
count_word_occurrences(splited)









