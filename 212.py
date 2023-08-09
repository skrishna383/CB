class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False
    def addword(self,word):
        cur=self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch]=TrieNode()
            cur=cur.children[ch]
        cur.word=True    
    def delword(self,word):
        cur=self
        path=[["",self]]
        for ch in word:
            cur=cur.children[ch]
            path.append([ch,cur])
        cur.word=False
        for i in range(len(path)-1,0,-1):
            ch,cur=path[i]
            if cur.word or cur.children: 
                break
            del path[i-1][1].children[ch]
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.addword(w)
        nr,nc=len(board),len(board[0])
        res,visit=set(),set()
        def dfs (r,c,node,word):
            if (r<0 or c<0 or r==nr or c==nc or (r,c)in visit or board[r][c] not in node.children):
                return 
            visit.add((r,c))
            node=node.children[board[r][c]]
            word=word+board[r][c]
            if node.word:
                res.add(word)
                root.delword(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        for r in range(nr):
            for c in range(nc):
                dfs (r,c,root,"")
        return list(res)
