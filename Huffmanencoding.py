class MinHeap:#Part of the MinHeap implementation uses codes from https://www.geeksforgeeks.org/min-heap-in-python/.

    class __Huffman_Node:#huffman node class
        def __init__(self, frequency, value, left, right):
            self.value = value#is None for inner nodes
            self.frequency = frequency
            self.left = left
            self.right = right

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.Heap = [self.__Huffman_Node(0,'', None, None)]*(self.capacity + 1)#initiate the heap as an array of huffman nodes.
        self.FRONT = 1# a constant to denote the root of heap
        self.Heap[0] = self.__Huffman_Node(-1,'',None, None)#the zero position is intended to be empty. In the huffman encoding, all frequency is larger than 0, so heap[0] always stays at the position.

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos//2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if pos > (self.size//2):# and pos <= self.size
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to heapify the node at pos
    def minHeapify(self, pos):

        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos].frequency > self.Heap[self.leftChild(pos)].frequency or
               self.Heap[pos].frequency > self.Heap[self.rightChild(pos)].frequency):

                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.rightChild(pos)].frequency < self.Heap[self.leftChild(pos)].frequency:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

    # Function to insert a node into the heap
    def insert(self, frequency, value, left, right):
        t = self.__Huffman_Node(frequency, value, left, right)
        if self.size >= self.capacity :
            return
        self.size+= 1
        self.Heap[self.size] = t
        current = self.size
        while self.Heap[current].frequency < self.Heap[self.parent(current)].frequency:
            self.swap(current, self.parent(current))
            current = self.parent(current)


    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)


    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped


    def merge(self):#remove t1, remove t2, merge them and insert it.
        while minHeap.size > 1:
            t1 = self.remove()
            t2 = self.remove()
            self.insert(t1.frequency+t2.frequency,None,t1,t2)

    def returnHuffmantree(self):#return root of the heap, which is the huffman tree after merging
        return self.Heap[1]


if __name__ == "__main__":
    data = input("type message to encode ")#prompt user for a text string
    corp = dict()
    for _ in data:
        corp[_]=corp.get(_,0)+1#build a dictionary to store the character and frequency
    minHeap = MinHeap(len(corp))#initiate a heap
    for x in sorted(corp):#insert all frequency and character into the min heap
        minHeap.insert(corp[x],x, None, None)
    minHeap.merge()#build a huffman tree with the heap. see explanation above
    def find_encoding_traversal(cur_node,encoding):#recursive method to find encoding for each character
          if cur_node.value is not None:#find character at root node, store the frequency as value of the key, which are charcters in the input string
              encodings[cur_node.value] = encoding
          else:
              find_encoding_traversal(cur_node.left,encoding +'0')#add a zero if going to left child
              find_encoding_traversal(cur_node.right,encoding +'1')#add a one if going to right child
    Huffmanroot = minHeap.returnHuffmantree()#After merging, the Huffman tree we want is at the root of heap.
    encodings = dict()
    for x in sorted(corp):
        encodings[x]=''#initialize the dictionary
    find_encoding_traversal(Huffmanroot,'')#store encodings into dictionary
    encoded_message = ''
    for c in data:
        encoded_message += encodings[c]#encode the message
    print(encoded_message)
    message_to_decode = input("type message to decode ")#prompt the user for a binary string
    decoded_message = ''
    character = Huffmanroot
    for c in message_to_decode:#decode it by going down the huffman tree. Should work if the binary string entered by user is valid.
        if c == '0':
            character = character.left
        else:
            character = character.right
        if character.value is not None:#when it reaches a leaf node in huffman tree
            decoded_message += character.value
            character = Huffmanroot
    print(decoded_message)
