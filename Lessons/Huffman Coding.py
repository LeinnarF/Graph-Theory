import heapq as hp

class Node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.huff = '' # tree direction

    def __lt__(self, other):
        return self.freq < other.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)

    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.char} = {newVal}")

# Characters and their frequencies in hash table
Hash = {'a': .2, 'b': .05, 'c': .1, 'd': .1, 'e': .25, 'f': .15, 'g':.15}

nodes = []

for char, freq in Hash.items():
    hp.heappush(nodes, Node(freq, char))

while len(nodes) > 1:
    left = hp.heappop(nodes)
    right = hp.heappop(nodes)

    left.huff = 0
    right.huff = 1

    newNode = Node(left.freq + right.freq, left.char + right.char, left, right)

    hp.heappush(nodes, newNode)

printNodes(nodes[0])

# Decode
def decodeHuffman(root, encoded_str):
    decoded_str = ''
    current = root
    for bit in encoded_str:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if not current.left and not current.right:
            decoded_str += current.char
            current = root
    return decoded_str

case1 = "0110011110001010"
case2 = "1110001101100011010"
case3 = "0101001100111110010"

print(decodeHuffman(nodes[0], case1))
print(decodeHuffman(nodes[0], case2))
print(decodeHuffman(nodes[0], case3))




