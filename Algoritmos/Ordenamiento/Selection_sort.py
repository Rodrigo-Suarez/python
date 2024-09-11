def selection_sort(array):
    n = len(array)
    for num in range(n-1):
        min_index = num
        for number in range(num+1, n):
            if array[number] < array[min_index]:
                min_index = number
        array[num], array[min_index] = array[min_index], array[num]

    return array


array = [9, 3, 4, 1, 5, 22]
print(selection_sort(array))