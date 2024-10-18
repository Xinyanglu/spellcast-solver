from collections import deque
class Path:
    def __init__(self):
        self.word = ''
        self.visited = set()
        self.visitedOrder = []
        self.score = 0

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.endOfWord

def createTrie():
    trie = Trie()
    with open('wordlist.txt') as f:
        for line in f:
            trie.insertWord(line.strip())
    return trie

points = {'a': 1, 'b': 4, 'c': 4, 'd': 2, 'e': 1, 'f': 4, 
          'g': 3, 'h': 3, 'i': 1, 'j': 10, 'k': 5, 'l': 2, 
          'm': 4, 'n': 2, 'o': 1, 'p': 4, 'q': 10, 'r': 1, 
          's': 1, 't': 1, 'u': 2, 'v': 5, 'w': 4,  'x': 8, 'y': 3, 'z': 10}

def scoreWord(word):
    score = 0
    for char in word:
        score += points[char]
    return score

def findBestPath(board, trie):
    maxPath = None
    currentPath = None
    frontier = deque()

    # DFS to find all possible words
    for row in range(5):
        for col in range(5):
            frontier.append(Path().visited(row,col))
            frontier[0].word = board[row][col]
            frontier[0].score = points[board[row][col]]
            frontier[0].visited.add((row,col))
            frontier[0].visitedOrder.append((row,col))

            while len(frontier) != 0:
                currentPath = frontier.pop()

                up = (currentPath.visitedOrder[-1][0], currentPath.visitedOrder[-1][1] - 1)
                down = (currentPath.visitedOrder[-1][0], currentPath.visitedOrder[-1][1] + 1)
                left = (currentPath.visitedOrder[-1][0] - 1, currentPath.visitedOrder[-1][1])
                right = (currentPath.visitedOrder[-1][0] + 1, currentPath.visitedOrder[-1][1])
                upLeft = (currentPath.visitedOrder[-1][0] - 1, currentPath.visitedOrder[-1][1] - 1)
                upRight = (currentPath.visitedOrder[-1][0] + 1, currentPath.visitedOrder[-1][1] - 1)
                downLeft = (currentPath.visitedOrder[-1][0] - 1, currentPath.visitedOrder[-1][1] + 1)
                downRight = (currentPath.visitedOrder[-1][0] + 1, currentPath.visitedOrder[-1][1] + 1)

                directions = (up, down, left, right, upLeft, upRight, downLeft, downRight)

                for direction in directions:
                    if direction[0] < 0 or direction[0] > 4 or direction[1] < 0 or direction[1] > 4:
                        continue
                    if direction in currentPath.visited:
                        continue
                    newWord = currentPath.word + board[direction[0]][direction[1]]
                    if not trie.startsWith(newWord):
                        continue
                    if trie.search(newWord):
                        if maxPath is None or currentPath.score > maxPath.score:
                            maxPath = currentPath
                    newPath = Path()
                    newPath.word = newWord
                    newPath.visited = set(currentPath.visited).add(direction)
                    newPath.visitedOrder = list(currentPath.visitedOrder).append(direction)
                    newPath.score = currentPath.score + points[board[direction[0]][direction[1]]]

                    frontier.append(newPath)

    return maxPath