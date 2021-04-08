def recur_max(s,start,stop):
    if start == stop:
        return s[start]
    elif s[start] >= s[stop]:
        return recur_max(s,start,stop - 1)
    else:
        return recur_max(s,start + 1,stop)
    
s = [5,2,4,1,8,6,12,7]
max = recur_max(s,0,len(s) - 1)