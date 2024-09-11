

def bubble_sort(array):
    length = len(array)
    for i in range(length - 1):
        is_swapped = False
        for num in range(length - 1 - i):
            if array[num] > array[num + 1]:
                array[num], array[num +1] = array[num + 1], array[num]
                is_swapped = True
        if not is_swapped:
            break
    return array
    


array = [4, 2, 6, 1, 7]
print(bubble_sort(array))