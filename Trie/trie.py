class TrieNode:
    def __init__(self,char=''):
        self.char = char
        self.children = [None] * 26
        self.is_end_word = False

    def mark_as_leaf(self):
        self.is_end_word = True

    def unmark_as_leaf(self):
        self.is_end_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self,t):
        return ord(t) - ord('a') #ord(): Given a string of length one,
    #returns an integer representing the Unicode code of the character.

    def insert(self, key):
        pass

    def delete(self, key):
        pass

    def search(self,key):
        pass

trie_node = TrieNode('a')
print(trie_node.char)
trie = Trie()
print(trie.get_index('f'))

