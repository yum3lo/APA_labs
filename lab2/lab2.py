import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

# Sorting algorithms
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

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

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   
        heapify(arr, i, 0)
    return arr

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Generate random input data sizes
input_sizes = list(range(100, 1100, 100))

# Sorting functions and their names
sort_functions = [quickSort, mergeSort, heapSort, selectionSort]
sort_names = ['QuickSort', 'MergeSort', 'HeapSort', 'SelectionSort']

# Collect execution times for each sorting algorithm
execution_times = np.zeros((len(sort_functions), len(input_sizes)))

for i, size in enumerate(input_sizes):
    input_data = [random.randint(1, 10000) for _ in range(size)]
    for j, sort_func in enumerate(sort_functions):
        total_time = 0
        for _ in range(10):  # Repeat 10 times for each algorithm
            start_time = time.time()
            sorted_data = sort_func(input_data.copy())
            end_time = time.time()
            total_time += (end_time - start_time)
        average_time = total_time / 10  # Calculate the average time
        execution_times[j][i] = average_time
        print(f"{sort_names[j]} with input size {size} was executed in {total_time:.6f} seconds")

# Plotting
plt.figure(figsize=(10, 6))

for i, sort_name in enumerate(sort_names):
    plt.plot(input_sizes, execution_times[i], marker='o', label=sort_name)

plt.xlabel('Input Size')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Performance of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()