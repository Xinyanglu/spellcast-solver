from solver import Trie, createTrie, findBestPath, findBestWord
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
        self.assertEqual(bestPath.word, 'absolute')

    def test_findBestWord(self):
        board = [['a','b','c','d','e'],
                 ['f','g','s','i','j'],
                 ['e','l','m','o','o'],
                 ['t','u','l','s','t'],
                 ['u','v','w','x','y']]
        
        resultBoard = [[1,2,'c','d','e'],
                       ['f','g',3,'i','j'],
                       [8,'l','m',4,'o'],
                       [7,6,5,'s','t'],
                       ['u','v','w','x','y']]
        
        bestWord = findBestWord(board)
        self.assertEqual(bestWord, 'absolute')
        self.assertEqual(board, resultBoard)

if __name__ == "__main__":
    unittest.main()