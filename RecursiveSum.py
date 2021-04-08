def recur_sum(arr):
    if arr == []:
        return 0
    return arr[0] + recur_sum(arr[1:])