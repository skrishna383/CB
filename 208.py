class TrieNode :
    def __init__(self):
        self.children={}
        self.endofword=False

class Trie:

    def __init__(self,val="",left=None,right=None):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
        curr.endofword=True

    def search(self, word: str) -> bool:
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr=curr.children[ch]
        return curr.endofword

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr=curr.children[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
#worst implimentation
class Trie:

    def __init__(self,val="",left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        

    def insert(self, word: str) -> None:
        if self.val=="":
            self.val=word
        else:
            if self.val>word:
                if self.left:
                    self.left.insert(word)
                else:
                    self.left=Trie(word)
            if self.val<word:
                if self.right:
                    self.right.insert(word)
                else:
                    self.right=Trie(word)
        

    def search(self, word: str) -> bool:
        if self.val==word:
            return True
        if not self.left and not self.right:
            return False
        if not self.left:
            return self.right.search(word)
        if not self.right:
            return self.left.search(word)
        return self.left.search(word) or self.right.search(word)

        

    def startsWith(self, prefix: str) -> bool:
        if self.val.startswith(prefix):
            return True
        if not self.left and not self.right:
            return False
        if not self.left:
            return self.right.startsWith(prefix)
        if not self.right:
            return self.left.startsWith(prefix)
        return self.left.startsWith(prefix) or self.right.startsWith(prefix)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)