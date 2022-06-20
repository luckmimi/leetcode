class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        self.word_set = []
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word):
        node = self.root
        for i,w in enumerate(word):
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
            node.word_set.append(word)
        node.is_word = True
        node.word = word
    def find(self,word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if node is None:
                return None
        return node
    def search(self,word):
        node = self.find(word)
        return node if node is not None and node.is_word else None
    def startWith(self, prefix):
        return self.find(prefix) is not None
    def find_word_set(self,prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_set
    
class Solution:
    def suggestedProducts(self, products: List[str], s: str) -> List[List[str]]:
        trie = Trie()
        for word in products:
            trie.add(word)
            print(trie.find_word_set(word))
        res = []
        for i in range(len(s)):
            st = trie.find_word_set(s[:i+1])
            st = sorted(st)
            if not st:
                res.append([])
            else:
                res.append(st[:3])
        return res
        
        
