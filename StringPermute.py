def permute(s,l,r):
    if l == r:
        for c in s:
            print(c,end = '')
        print('\n')
    else:
        for i in range(l,r + 1):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]
#
# Main
s = "abc"
s = list(s)
permute(s, 0, len(s) - 1)