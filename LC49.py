class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = collections.defaultdict(list)
        for word in strs:
            cur = ''.join(sorted(word))
            c[cur].append(word)
        return c.values()
