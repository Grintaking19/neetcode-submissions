class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = "".join(filter(str.isalnum,s)).lower()
        return filtered_string == filtered_string[::-1]