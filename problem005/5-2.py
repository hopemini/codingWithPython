def strStr(haystack, needle):
    len_haystack = len(haystack)
    len_needle = len(needle)
    if len_haystack < len_needle:
        return -1;
    if len_haystack == 0 or len_needle == 0:
        return 0;  
    for i in range(len_haystack - len_needle + 1):
        if haystack[i:i+len_needle] == needle:
            return i     
    return -1

    #if haystack == needle:
    #    return 0
    #for i in range(len(haystack)):
    #    if haystack[i:].startswith(needle):
    #        return i
    #return -1

h = input()
n = input()

print(strStr(h, n))
