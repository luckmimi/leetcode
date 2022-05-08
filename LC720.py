class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        self.height = 0 
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
            node.height =  i + 1
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
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        max_height = 0
        res = ''
        for word in words:
            trie.insert(word)
        q = collections.deque([(trie.get_root())])
        while q:
            node= q.popleft()
            # print(node.word, end = ',')
            if node != trie.get_root() and not node.is_word: continue
            if node.height> max_height:
                    res = node.word
                    max_height = node.height
            elif node.height == max_height and res != '' and res > node.word:
                res = node.word
            # print(f'res:{res}, path:{path}')
            for char in  node.children:
                        q.append((node.children[char]))
        return res
        
