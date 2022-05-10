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
        node.word = word
        node.is_word = True
    # def find(self,word):
    #     node = self.root
    #     for c in word:
    #         node = node.children.get(c)
    #         if not node:
    #             return None
    #     return node
    # def search(self,word):
    #     node = self.find(word)
    #     return node is not None and node.is_word
    # def startWith(self,prefix):
    #     return self.find(prefix) is not None
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        self.res = []
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board,i,j,'',trie.get_root())        
        return self.res
    def dfs(self,board, i, j,path, node):
            if node.is_word:
                self.res.append(path)
                node.is_word = False
                
            if not self.is_valid(board,i,j):
                return
            tmp = board[i][j]
            parent = node
            node = node.children.get(tmp)
            if not node:
                    return
            board[i][j] = '#'
            for dx, dy in ((0,1),(0,-1),(-1,0),(1,0)):
                newx = i + dx
                newy = j + dy
                
                
                self.dfs(board, newx,newy, path + tmp,node)
            if len(node.children) == 0:
                del parent.children[tmp]
            board[i][j] = tmp
                
           
    def is_valid(self,board,x,y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == "#":
            return False
        return True
