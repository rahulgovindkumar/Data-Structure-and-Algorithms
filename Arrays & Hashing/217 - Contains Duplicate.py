"""
Problem #1 {Easy} 

217. Contains Duplicate

Time Complexity O(n)
Space Complexity:  O(n)

Did this code successfully run on Leetcode : Yes

Approach 1: Using hashset
    TC: O(n)
    SC: O(n)
    
 
Approach 2: Using For loop (Check each element)
    TC: O(n*n)
    SC: O(1)

Approach 3: Sort The element _ Approach 1
    TC: O(n*log n)
    SC: O(1)


https://leetcode.com/problems/contains-duplicate/

@name: Rahul Govindkumar
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        n = len(nums)
        twin = set()  # Create an empty set to store visited values.
        count = 0     # Keep track of the number of duplicates found.
        
        for val in nums:
            # If a value is already in the set, it's a duplicate.
            if val in twin:
                count += 1
                twin.remove(val)  # Remove the duplicate value from the set.
                break  # No need to continue the loop, we found a duplicate.
            else:
                twin.add(val)  # Add the new value to the set.
                
        # If we found at least one duplicate, return True.
        if count:
            return True
        else:
            return False