def recur_count(arr):
    if arr == []:
        return 0
    return 1 + recur_count(arr[1:])