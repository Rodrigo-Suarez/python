""" 
def quick_sort(array, pivot = None):
    
    array_2 = []

    if pivot == None:
        pivot = len(array) - 1

    for num in range(pivot):
        if array[num] > array[pivot]:
            array_2.append(array.pop(num))
    
    array.append(array_2)
        
    return array


array = [9, 1, 3, 2, 55, 23, 5, 11]
print(quick_sort(array))
 """

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)