import random
import time
import matplotlib.pyplot as plt

# Generate random input data
input_data = [random.randint(1, 1000000) for _ in range(10000)]

# QuickSort algorithm
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

# MergeSort algorithm
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result

# HeapSort algorithm
def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i]) 
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])   
        heapify(arr, i, 0)

    return arr

# Selection Sort algorithm
def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Measuring the time for each sorting algorithm
sort_functions = [quickSort, mergeSort, heapSort, selectionSort]
sort_names = ['QuickSort', 'MergeSort', 'HeapSort', 'SelectionSort']
execution_times = []

for sort_func in sort_functions:
    start_time = time.time()
    sorted_data = sort_func(input_data.copy())
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    print(f"{sort_func.__name__} executed in {execution_time:.6f} seconds.")

# Plot for all algorithms
plt.bar(sort_names, execution_times, color=['tab:blue', 'tab:orange', 'tab:brown', 'tab:purple'])
plt.xlabel('Sorting Algorithms')
plt.ylabel('Execution Time (seconds)')
plt.title('Performance of Sorting Algorithms')
plt.show()