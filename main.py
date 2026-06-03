from collections import Counter
import heapq
import os


class Node:

    def __init__(self, char, freq):

        self.char = char
        self.freq = freq

        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def read_file(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print("File not found!")
        return None


def build_frequency_table(text):
    return Counter(text)


def build_min_heap(frequency):

    heap = []

    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    return heap


def build_huffman_tree(heap):

    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)

        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, current_code, codes):

    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)


def compress_text(text, codes):

    compressed = ""

    for char in text:
        compressed += codes[char]

    return compressed


def decompress_text(compressed_text, codes):

    reverse_codes = {}

    for char, code in codes.items():
        reverse_codes[code] = char

    current_code = ""
    decompressed = ""

    for bit in compressed_text:

        current_code += bit

        if current_code in reverse_codes:

            decompressed += reverse_codes[current_code]
            current_code = ""

    return decompressed


def calculate_compression_ratio(original_text, compressed_text):

    original_bits = len(original_text) * 8

    compressed_bits = len(compressed_text)

    ratio = (compressed_bits / original_bits) * 100

    return original_bits, compressed_bits, ratio


def main():

    file_path = "input_files/sample.txt"

    text = read_file(file_path)

    if text:

        frequency = build_frequency_table(text)

        heap = build_min_heap(frequency)

        root = build_huffman_tree(heap)

        codes = {}

        generate_codes(root, "", codes)

        compressed_text = compress_text(text, codes)

        decompressed_text = decompress_text(
            compressed_text,
            codes
        )

        os.makedirs("compressed_files", exist_ok=True)
        os.makedirs("decompressed_files", exist_ok=True)

        with open(
            "compressed_files/compressed.txt",
            "w",
            encoding="utf-8"
        ) as file:
            file.write(compressed_text)

        with open(
            "decompressed_files/decompressed.txt",
            "w",
            encoding="utf-8"
        ) as file:
            file.write(decompressed_text)

        original_bits, compressed_bits, ratio = (
            calculate_compression_ratio(
                text,
                compressed_text
            )
        )

        print("\nCompression Successful!")
        print("\nDecompression Successful!")

        if text == decompressed_text:

            print("\nVerification Successful!")

            print("\nCompression Report")
            print("-" * 30)

            print(f"Original Size   : {original_bits} bits")
            print(f"Compressed Size : {compressed_bits} bits")
            print(f"Compression Ratio : {ratio:.2f}%")

        else:
            print("\nVerification Failed!")


if __name__ == "__main__":
    main()