import heapq
import os

class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

    def makeFrequencyDict(self, text):
        frequency = {}
        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency

    def makeHeap(self, frequency):
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def buildHuffmanTree(self):
        root = self.HeapNode(None, 0)
        root.left = self.heap[0]
        self.mergeNodes()
        return root
    
    def mergeNodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)

    def buildHuffmanCodes(self, node, current_code):
        if node is None:
            return
        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
        self.buildHuffmanCodes(node.left, current_code + "0")
        self.buildHuffmanCodes(node.right, current_code + "1")

    def getEncodedText(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    def padEncodedText(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"
        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def getByteArray(self, padded_encoded_text):
        if len(padded_encoded_text) % 8 != 0:
            raise ValueError("Encoded text is not properly padded")
        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            b.append(int(byte, 2))
        return b

    def compress(self, text, output_file):
        frequency = self.makeFrequencyDict(text)
        self.makeHeap(frequency)
        self.mergeNodes()
        root = self.buildHuffmanTree()
        self.buildHuffmanCodes(root, "")
        encoded_text = self.getEncodedText(text)
        padded_encoded_text = self.padEncodedText(encoded_text)
        byte_array = self.getByteArray(padded_encoded_text)
        with open(output_file, "wb") as f:
            f.write(bytes(byte_array))
        print("Compression completed successfully.")

    def decompress(self, input_file, output_file):
        with open(input_file, "rb") as f:
            bit_string = ""
            byte = f.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = f.read(1)
            extra_padding = int(bit_string[:8], 2)
            bit_string = bit_string[8:]
            encoded_text = bit_string[:-1 * extra_padding]
            
            current_code = ""
            decoded_text = ""
            for bit in encoded_text:
                current_code += bit
                if current_code in self.reverse_mapping:
                    character = self.reverse_mapping[current_code]
                    decoded_text += character
                    current_code = ""
        with open(output_file, "w") as f:
            f.write(decoded_text)
        print("Decompression completed successfully.")

if __name__ == "__main__":
    huffman = HuffmanCoding()
    input_file = "in.txt"
    output_file = "out.txt"
    compressed_file = "compress.bin"

    with open(input_file, "r") as file:
        text = file.read()

    if len(text) > 0:
        huffman.compress(text, compressed_file)
        huffman.decompress(compressed_file, output_file)

        initial_size = os.path.getsize(input_file)
        compressed_size = os.path.getsize(compressed_file)
        print(f"Initial file size: {initial_size} bytes")
        print(f"Compressed file size: {compressed_size} bytes")
    else:
        print("empty")
