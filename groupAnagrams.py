from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)

        for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-ord('a')]+=1
            key=tuple(count)
            anagrams[key].append(i)
        return anagrams.values()
                

if __name__ == "__main__":
    sol=Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))