def lengthOfLongestSubstring(s):
    max_len = 0
    i = 0
    j = 0
    l = []
    while j < len(s):
        if s[j] not in l:
            l.append(s[j])
            j += 1
        else:
            l.pop(0)
            l.append(s[j])
            j += 1
            print(l)
            max_len = max(max_len,len(l))
    return max_len

res = lengthOfLongestSubstring('alqebriavxoo')
print(res)