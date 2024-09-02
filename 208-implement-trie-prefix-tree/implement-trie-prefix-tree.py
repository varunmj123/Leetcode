class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class Trie:  # Change PrefixTree to Trie as per the problem statement

    def __init__(self):
        self.rootNode = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.rootNode
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endWord = True 

    def search(self, word: str) -> bool:
        curr = self.rootNode
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.rootNode
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
