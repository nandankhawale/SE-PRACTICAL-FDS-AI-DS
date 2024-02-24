
"""Write a Python program to maintain club members, sort on roll numbers in ascending 
order. Write function “Ternary_Search” to search whether particular student is member 
of club or not.  Ternary search is modified binary search that divides array into 3 halves 
instead of two."""

import array as arr

n = int(input("Enter the number of persons present in the club: "))
clubmember = arr.array('i', ())

for i in range(n):
    rolo = int(input("Enter the roll number in the club: "))
    clubmember.append(rolo)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        flag=0
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                flag=1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if (flag==0):
            break
    return arr

sorted_members = bubbleSort(clubmember)
print("Sorted roll numbers:", sorted_members)

target=int(input("Enter the roll no to be searched:- "))
l=0
r=len(clubmember)-1

def ternary_search(l, r, key, ar):

  if r >= l:
    # Find the mid1 and mid2.
    mid1 = l + (r - l) // 3
    mid2 = r - (r - l) // 3

    # Check if key is present at any mid.
    if ar[mid1] == key:
      return mid1
    if ar[mid2] == key:
      return mid2

    if key < ar[mid1]:
      return ternary_search(l, mid1 - 1, key, ar)
    elif key > ar[mid2]:
      return ternary_search(mid2 + 1, r, key, ar)
    else:
      return ternary_search(mid1 + 1, mid2 - 1, key, ar)

  # Key not found.
  return -1

result = ternary_search(l, r, target,clubmember)

if result != -1:
  print(f"The key  is found at index {result} ")
else:
  print("The key is not found in the array.")






