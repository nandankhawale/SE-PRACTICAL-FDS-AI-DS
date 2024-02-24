


""" Write a Python program to store first year percentage of students in array. Write 
function for sorting array of floating point numbers in ascending order using quick sort 
and display top five scores"""



import array as arr

mark = arr.array('d', ())
n = int(input("Enter the number of students in the first year: "))

for i in range(n):
    percentage = float(input("Enter the percentage obtained in the first year: "))
    mark.append(percentage)
    

    
def quicksort(arr, low, high):
    if low < high:
        pivot_location = partition(arr, low, high)
        quicksort(arr, low, pivot_location - 1)
        quicksort(arr, pivot_location + 1, high)
        
        
def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    arr[low], arr[right] = arr[right], arr[low]
    return right

left = 0
right = len(mark) - 1

quicksort(mark, left, right)

print("Array after quicksort:", mark)

for percentage in mark[-5:][::-1]:
    print(percentage)






