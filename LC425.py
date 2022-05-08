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
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        results, square = [], []
        for word in words:
            square.append(word)
            self.dfs(square, len(word), results,trie)
            square.pop()
        return results
    def dfs(self,square,n,results, trie):
        curr_len = len(square)
        if curr_len == n:
            results.append(square.copy())
            return
        prefix = ''.join([square[i][curr_len] for i in range(curr_len)])
        for row in trie.get_word_set(prefix):
            square.append(row)
            self.dfs(square, n, results, trie)
            square.pop()
