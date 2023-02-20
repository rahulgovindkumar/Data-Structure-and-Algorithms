"""
Problem #2 {Easy} 

242. Valid Anagram

Time Complexity O(n)
Space Complexity:  O(n)

Did this code successfully run on Leetcode : Yes

Approach 1: Using hashmap
    TC: O(n)
    SC: O(n)
    
 
Approach 2: Using Sort (Check each element)
    TC: O(n*log n)
    SC: O(1)




https://leetcode.com/problems/valid-anagram/

@name: Rahul Govindkumar
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Check if the length of the two strings is equal
        if len(s) != len(t):
            return False
        
        # Create a hashmap to store the frequency of each character in string s
        hashmap = {}
        for ch in s:
            hashmap[ch] = 1 + hashmap.get(ch, 0)
            
        # Iterate through each character in string t and remove it from the hashmap
        # If the character is not present in the hashmap or its frequency becomes zero, return False
        for ch in t:
            if ch in hashmap:
                hashmap[ch] -= 1
                if hashmap[ch] == 0:
                    hashmap.pop(ch)
            else:
                return False
            
        # If all characters in t have been processed and hashmap is empty, return True
        return len(hashmap) == 0