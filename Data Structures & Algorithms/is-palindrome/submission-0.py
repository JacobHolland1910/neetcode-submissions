class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter_list = list(s.strip().lower())
        l = 0 
        r = len(letter_list) - 1

        while l <= r:
            if s[l].isalnum() and s[r].isalnum():
                if letter_list[l] == letter_list[r]:
                    l += 1
                    r -= 1
                else:return False
            elif s[l].isalnum() == False:
                l += 1
            elif s[r].isalnum() == False:
                r -= 1
                
        return True

        