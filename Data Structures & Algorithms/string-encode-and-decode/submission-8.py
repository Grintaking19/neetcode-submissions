class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedS = ""
        for s in strs:
            encodedS = encodedS + str(len(s)) + "#" + s
        return encodedS
    
    def decode(self, s: str) -> List[str]:
        result = []
        print(s)
        i = 0
        while i < len(s):
            j = 0
            while s[i+j] != "#":
                j+=1
            word_len = int(s[i:i+j])
            start_word = i + j + 1
            end_word = start_word + word_len
            result.append(s[start_word : end_word])
            i = end_word
        return result