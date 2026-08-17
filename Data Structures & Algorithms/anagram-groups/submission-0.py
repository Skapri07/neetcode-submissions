from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        saraKapri = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))

            saraKapri[key].append(word)
        
        return list(saraKapri.values())







         


        