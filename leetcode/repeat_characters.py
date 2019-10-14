def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
        return 0
    max_len, cur_len, lookup = 0, 0, []
    for i in range(len(s)):
        cur_len += 1
        if s[i] in lookup:
            idx = lookup.index(s[i])
            l = len(lookup)
            if l - 1 == idx:
                lookup = []
                cur_len = 1
            else:
                lookup = lookup[idx + 1:l]
                cur_len -= idx + 1
        max_len = max(max_len, cur_len)
        lookup.append(s[i])
    return max_len