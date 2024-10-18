from solver import Trie, createTrie, findBestPath
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

    def test_findBestPath(self):
        trie = createTrie()
        board = [['a','b','c','d','e'],
                 ['f','g','s','i','j'],
                 ['e','l','m','o','o'],
                 ['t','u','l','s','t'],
                 ['u','v','w','x','y']]
        
        bestPath = findBestPath(board, trie)
        print(bestPath.word)
        print(bestPath.visitedOrder)
        self.assertEqual(bestPath.word, 'absolute')

if __name__ == "__main__":
    unittest.main()