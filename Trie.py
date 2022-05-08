class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        sef.max_height = 0 
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
        return node if node is not None and node.is_word
    def startWith(self,prefix):
        return self.find(prefix) is not None 
