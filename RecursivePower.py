def recur_power(x,n):
    if n == 0:
        return 1
    else:
        partial = recur_power(x,n // 2)
        result = partial * partial
        if n % 2 != 0:
            result *= x
        return result

d = recur_power(2,2)