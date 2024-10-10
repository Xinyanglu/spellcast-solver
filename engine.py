import imageprocess
import collections

class Node:
    def __init__(self):
        self.position = (0,0)

class Trie:
    def __init__(self):
        self.trie = { '' : { } }

    def insertWord(self, word):
        currentLevel = self.trie['']
        for l in word.lower():
            if l not in currentLevel:
                currentLevel[l] = { }
            
            currentLevel = currentLevel[l]

        currentLevel['end'] = ''

    def printTrie(self):
        print(self.trie)
