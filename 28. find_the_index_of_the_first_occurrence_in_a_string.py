# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
#
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

def strStr(haystack: str, needle: str):
    if needle == "":
        return 0

    # for i in range(len(haystack) + 1 - len(needle)):
    #     if haystack[i: i + len(needle)] == needle:
    #         return i
    for i in range(len(haystack) + 1 - (len(needle))):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i
    return -1


strStr("sadbutsad", "sad")
strStr("leetcode", "leeto")
