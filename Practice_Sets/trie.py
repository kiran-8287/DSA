class TrieNode:
    """A node in the Trie."""
    def __init__(self):
        self.children = {}     # dictionary to store child nodes
        self.is_end_of_word = False  # marks the end of a valid word


class Trie:
    """Trie Data Structure."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Inserts a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Returns True if word exists in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """Returns True if there exists any word with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def _collect_all_words(self, node=None, prefix="", words=None):
        """Helper method to collect all words from a given node."""
        if words is None:
            words = []
        if node is None:
            node = self.root

        if node.is_end_of_word:
            words.append(prefix)

        for char, child in node.children.items():
            self._collect_all_words(child, prefix + char, words)

        return words

    def autocomplete(self, prefix):
        """Returns all words in the trie that start with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # prefix not found
            node = node.children[char]

        return self._collect_all_words(node, prefix)

trie = Trie()
words = ["apple", "app", "application", "banana", "bat", "batch", "batman"]
for w in words:
    trie.insert(w)

print(trie.search("apple"))        # True
print(trie.search("apples"))       # False
print(trie.starts_with("app"))     # True
print(trie.autocomplete("bat"))    # ['bat', 'batch', 'batman']
