'''
	Program: Two Sum
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
	You may assume that each input would have exactly one solution, and you may not use the same element twice.
	courtesy: Leetcode   
'''


# solution-01
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_storage = {}
        for index, value in enumerate(nums):
            pair = target - value
            if pair in map_storage:
                return [map_storage[pair], index]
            # assuming there is atleast one solution 
            map_storage[value] = index