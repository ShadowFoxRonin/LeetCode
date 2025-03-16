from typing import List


def longest_common_prefix(strs: List[str]):
    if len(strs) == 0:
        return ""
    if len(strs)==1:
        return strs[0]
    strs.sort(key= lambda x: len(x))
    res = strs[0]
    str_len = len(res)
    strs.remove(res)
    for i in range(str_len):
        for s in strs:
            if res[i] != s[i]:
                return res[:i]

    return res


print(longest_common_prefix(["",""]))
