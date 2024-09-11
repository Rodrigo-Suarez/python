def insertion_sort(array):
    n = len(array)
    for num in range(1, n):
        insert_index = num
        current_value = array[num]
        for number in range(num-1, -1, -1):
            if array[number] > current_value:
                array[number + 1] = array[number]
                insert_index = number
            else:
                break  
        array[insert_index] = current_value

    return array

array = [9, 4, 6, 3, 4, 66, 35]
print(insertion_sort(array))