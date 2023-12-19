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

    # Функція для побудови таблиці частоти входження символів
    def buildFrequencyTable(self, text):
        frequency = {}
        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency

    # Функція для створення черги пріоритетів на основі таблиці частоти
    def buildHeap(self, frequency):
        for char, freq in frequency.items():
            node = self.HeapNode(char, freq)
            heapq.heappush(self.heap, node)

    # Функція для побудови дерева Хаффмана
    def buildHuffmanTree(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged_node = self.HeapNode(None, node1.freq + node2.freq)
            merged_node.left = node1
            merged_node.right = node2

            heapq.heappush(self.heap, merged_node)

    # Функція для кодування символів
    def buildHuffmanCodes(self, root, current_code):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char

        self.buildHuffmanCodes(root.left, current_code + "0")
        self.buildHuffmanCodes(root.right, current_code + "1")

    # Функція для кодування тексту
    def encode(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    # Функція для декодування тексту
    def decode(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                char = self.reverse_mapping[current_code]
                decoded_text += char
                current_code = ""

        return decoded_text

    # Функція для стискання текстового файлу та збереження результатів
    def compress(self, input_file, output_file):
        with open(input_file, 'r') as file:
            text = file.read()
        
        frequency = self.buildFrequencyTable(text)
        self.buildHeap(frequency)
        self.buildHuffmanTree()
        self.buildHuffmanCodes(self.heap[0], "")

        encoded_text = self.encode(text)

        with open(output_file, 'wb') as file:
            file.write(bytes(encoded_text, 'utf-8'))

        print("Compression complete.")

    # Функція для розпакування текстового файлу та збереження результатів
    def decompress(self, input_file, output_file):
        with open(input_file, 'rb') as file:
            encoded_text = file.read().decode('utf-8')

        decoded_text = self.decode(encoded_text)

        with open(output_file, 'w') as file:
            file.write(decoded_text)

        print("Decompression complete.")

    # Функція для визначення розміру файлу
    def get_file_size(self, filename):
        return os.path.getsize(filename)

# Приклад використання класу HuffmanCoding
if __name__ == '__main__':
    huffman = HuffmanCoding()
    
    # Визначення розміру файлу до стискання
    input_file_size = huffman.get_file_size('in.txt')
    print(f"Розмір вихідного файлу: {input_file_size} байт")

    huffman.compress('in.txt', 'compress.bin')
    
    # Визначення розміру файлу після стискання
    compressed_file_size = huffman.get_file_size('compress.bin')
    print(f"Розмір стиснутого файлу: {compressed_file_size} байт")

    huffman.decompress('compress.bin', 'out.txt')
