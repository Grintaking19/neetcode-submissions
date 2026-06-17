class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            curr = 1
            for j in range(i+1, len(s)):
                if len(set(s[i:j+1])) != len(s[i: j+1]):
                    break
                curr +=1
                # print(s[i: j+1], curr)
            longest = max(longest, curr)    
        return longest
