# Problem 242: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy

# Approach: Using a dictionary to count the frequency of characters in both strings.
# If the frequency counts are equal, the strings are anagrams.
# Time: O(n) | Space: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sf, tf = {}, {}
        if len(s) != len(t):
            return False
        for char in s:
            sf[char] = sf.get(char, 0) + 1
        for char in t:
            tf[char] = tf.get(char, 0) + 1
        if sf == tf:
            return True
        return False