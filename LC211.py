class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def get_root(self):
        return self.root
    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word
    def find(self,word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return None
        return node
    def search(self,word):
        node = self.find(word)
        return node is not None and node.is_word
    def startWith(self,prefix):
        return self.find(prefix) is not None
class WordDictionary:

    def __init__(self):
        self.dict = Trie()

    def addWord(self, word: str) -> None:
        self.dict.insert(word)

    def search(self, word: str) -> bool:
        def dfs(word, node,pos):
            if not node:
                return False
            if pos == len(word):
                return node.is_word
            cur = word[pos]
            if cur == '.':
                for child in node.children:
                        if dfs(word,node.children[child],pos + 1):
                            return True
            else:
                node = node.children.get(cur)
                if not node:
                    return False
                return dfs(word,node,pos + 1)
                  
            return False
        return dfs(word,self.dict.get_root(),0)
    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
