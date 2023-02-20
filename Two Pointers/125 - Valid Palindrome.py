"""
Problem #4 {Easy} 

125. Valid Palindrome


Did this code successfully run on Leetcode : Yes

Approach 1: Using Two Pointer
    TC: O(n)
    SC: O(n)
    


https://leetcode.com/problems/valid-palindrome/

@name: Rahul Govindkumar
"""

class Solution:
    
    def alphaNum(self,ch):
        
        return ( ord('A') <= ord(ch) <= ord('Z') or
                 ord('a') <= ord(ch) <= ord('z') or
                 ord('0') <= ord(ch) <= ord('9') )
    
    def isPalindrome(self, s: str) -> bool:
        
        # get the length of the string
        n = len(s)

        # if the string has only one character, it's a palindrome
        if n == 1:
            return True

        # initialize left and right pointers
        l = 0
        r = n - 1

        # loop until the pointers meet in the middle
        while l < r:

            # if the left character is not alphanumeric, skip it
            if not self.alphaNum(s[l]):
                l += 1
                continue

            # if the right character is not alphanumeric, skip it
            if not self.alphaNum(s[r]):
                r -= 1
                continue

            # convert the left and right characters to lowercase and compare them
            ch_l = s[l].lower() 
            ch_r = s[r].lower()    
            if ch_l != ch_r:
                return False

            # move the pointers inward
            l += 1
            r -= 1

        # if the function has not returned False yet, the string is a palindrome
        return True