def group_anagrams(strs):
    anagrams = {}
    strs_len = len(''.join(strs))
    for i in range(strs_len):
        sorted_str = ''.join(sorted(strs[i]))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(strs[i])
        else:
            anagrams[sorted_str] = [strs[i]]
    return list(anagrams.values())
