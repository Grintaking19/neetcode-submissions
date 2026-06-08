class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        result = []
        text_dict = {}
        for i in range(len(strs)):
            sorted_text = "".join(sorted(strs[i]))
            if sorted_text in text_dict:
                text_dict[sorted_text].append(strs[i])
            else: 
                text_dict[sorted_text] = [strs[i]]
        
        return list(text_dict.values())
