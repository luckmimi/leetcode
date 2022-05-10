class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        self.max_height = 0 
        self.word_set = []
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def get_root(self):
        return self.root
    def insert(self,word):
        node = self.root
        for i,c in enumerate(word):
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.max_height = max(node.max_height, len(word) - i - 1)
            node.word_set.append(word)
        node.is_word = True
        node.word = word
    def find(self,word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node
    def get_word_set(self,prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_set
    def search(self,word):
        node = self.find(word)
        return node is not None and node.is_word
    def startWith(self,prefix):
        return self.find(prefix) is not None 

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        import bisect
        def isMatched(word):
            if word in mp: return mp[word]
            last_index = -1
            for c in word:
                p = pos[c]
                index = bisect.bisect_left(p,last_index + 1)
                #index = self.search(p, last_index + 1)
                #print(index, index_)
                if index == len(p):
                    mp[word] = 0 
                    return 0
                last_index = pos[c][index]
            mp[word] = 1
            return 1
        
        
        mp = {}
        pos = collections.defaultdict(list)
        for i,c in enumerate(s):
            pos[c].append(i)
        
        return sum(map(isMatched,words))
                
    def search(self,arr, pos):
        left = 0
        right = len(arr) - 1
        if right < 0 : return len(arr)
        # print('before search',left, len(arr), right)
        while left + 1 < right:
            mid = left + (right - left) //2
            if arr[mid] < pos:
                left = mid
            else:
                right = mid 
        # print('search',left, len(arr), right)
        if arr[left] >= pos:
            return left
        if arr[right] >= pos:
            return right
        return len(arr)
                
            
