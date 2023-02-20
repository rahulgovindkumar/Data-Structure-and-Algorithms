"""
Problem #3 {Easy} 

1. Two Sum

Time Complexity O(n)
Space Complexity:  O(n)

Did this code successfully run on Leetcode : Yes

Approach 1: Using hashmap
    TC: O(n)
    SC: O(n)
    


https://leetcode.com/problems/two-sum/

@name: Rahul Govindkumar
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # create a dictionary to store the indices of each number in the list
        # keys are numbers, values are their indices
        hashmap = {}
        
        # loop through the list of numbers
        n = len(nums)
        for i in range(n):
            
            # calculate the difference between the target and the current number
            diff = target - nums[i] 
            
            # if the difference is already in the dictionary, we've found a pair that adds up to the target
            if diff in hashmap:
                
                # return a list of the indices of the two numbers that add up to the target
                return [hashmap[diff], i]
            
            # if the difference is not in the dictionary, add the current number and its index to the dictionary
            else:
                hashmap[nums[i]] = i
                
        
        