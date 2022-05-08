class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.is_word = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word
        node.is_word = True
                
    def find (self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return None
        return node
    def search(self, word: str) -> bool:
        node = self.find(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        
        return  self.find(prefix) is not None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
