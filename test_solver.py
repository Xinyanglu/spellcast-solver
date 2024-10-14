from solver import Trie, createTrie
import unittest

class TestTrie(unittest.TestCase):
    def test_insertWord(self):
        trie = Trie()
        trie.insertWord("hello")
        self.assertTrue(trie.search("hello"))
        self.assertFalse(trie.search("hell"))

    def test_startsWith(self):
        trie = Trie()
        trie.insertWord("hello")
        self.assertTrue(trie.startsWith("hell"))
        self.assertFalse(trie.startsWith("heaven"))

    def test_search(self):
        trie = Trie()
        trie.insertWord("hello")
        self.assertTrue(trie.search("hello"))
        self.assertFalse(trie.search("hell"))
        self.assertFalse(trie.search("helloo"))

    def test_createTrie(self):
        trie = createTrie()
        self.assertTrue(trie.search("vainglorious"))
        self.assertTrue(trie.search("phosphatic"))
        self.assertTrue(trie.search("zymometer"))
        self.assertTrue(trie.startsWith("vaingl"))
        self.assertFalse(trie.search("vaingloriouss"))
        self.assertFalse(trie.startsWith("hv"))

if __name__ == "__main__":
    unittest.main()