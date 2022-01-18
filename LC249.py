class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def helper(s):
            dst = ord(s[0]) - ord('a')
            arr = list(s)
            arr[0] = 'a'
            for i in range(1,len(s)):
                d = ord(s[i]) -  dst
                if d < 97:
                     d += 26
                arr[i] = chr(d)
            return ''.join(arr)
        group = dict()
        for s in strings:
            cur = helper(s)
            if cur in group:
                group[cur].append(s)
            else:
                group[cur] =  [s]
        # print(group)
        return group.values()
                
