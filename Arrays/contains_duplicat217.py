# Problem 217: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy

# Approach: Use a set to track seen numbers.
# If a number is already in the set, duplicate found.
# Time: O(n) | Space: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            else:
                num_set.add(i)
        return False