class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.is_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
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
    def get_root(self):
        return self.root
        
class MagicDictionary:

    def __init__(self):
        self.trie = Trie()
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)
        

    def search(self, searchWord: str) -> bool:
        root = self.trie.get_root()
        q = collections.deque([root])
        while q:
           
            node = q.popleft()

            for c in node.children:
                    q.append(node.children[c])
            if node.word:
                if self.is_valid(node.word, searchWord):
                    return True
        # return False
    def is_valid(self,word, target):
        
        if len(word) != len(target) or word == target:
            return False
        cnt = 0
        for i,c in enumerate(target):
            if c != word[i]:
                cnt += 1
        return cnt == 1


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
