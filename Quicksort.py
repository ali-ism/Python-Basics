def qsort(array):
    if len(array) < 2:
        return array
    mid = (len(array) - 1) // 2
    pivot = array[mid]
    lesser = [elem for elem in array[:mid] if elem <= pivot]
    lesser.extend([elem for elem in array[mid + 1:] if elem <= pivot])
    greater = [elem for elem in array[:mid] if elem >= pivot]
    greater.extend([elem for elem in array[mid + 1:] if elem >= pivot])
    return qsort(lesser) + [pivot] + qsort(greater)