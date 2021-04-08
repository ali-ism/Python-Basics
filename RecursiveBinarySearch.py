def binary_search(array,elem):
    arr = sorted(array)
    mid_index = (len(arr) - 1)//2
    mid = arr[mid_index]
    if mid == elem:
        return mid_index
    elif mid < elem:
        return binary_search(arr[mid_index + 1:],elem) + mid_index + 1
    else:
        return binary_search(arr[:mid_index - 1],elem) + mid_index + 1