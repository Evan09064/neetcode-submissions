class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            fingerprint = "".join(sorted(word))
            if fingerprint in groups:
                groups[fingerprint].append(word)
            else:
                groups[fingerprint] = [word]
        return list(groups.values())