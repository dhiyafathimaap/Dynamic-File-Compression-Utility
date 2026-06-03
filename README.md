# Dynamic File Compression Utility

## Project Overview

Dynamic File Compression Utility is a Data Structures and Algorithms project that implements Huffman Coding for lossless file compression and decompression.

The project reads text data, calculates character frequencies, constructs a Huffman Tree using a Min Heap (Priority Queue), generates binary codes, compresses the file, and restores the original file through decompression.

---

## Problem Statement

Large files consume storage space and increase transmission costs.

The goal of this project is to reduce file size using Huffman Coding while ensuring that the original data can be perfectly recovered.

---

## Features

* File Reading
* Character Frequency Analysis
* Huffman Tree Construction
* Min Heap Implementation
* Huffman Code Generation
* File Compression
* File Decompression
* Compression Ratio Analysis
* Verification of Data Integrity

---

## DSA Concepts Used

### Hash Map (Dictionary)

Used to store character frequencies.

### Min Heap (Priority Queue)

Used to efficiently retrieve minimum-frequency nodes.

### Binary Tree

Used to construct the Huffman Tree.

### Greedy Algorithm

Huffman Coding repeatedly combines the least frequent nodes to achieve optimal compression.

---

## Project Workflow

Input File
↓
Frequency Table Creation
↓
Min Heap Construction
↓
Huffman Tree Creation
↓
Huffman Code Generation
↓
Compression
↓
Decompression
↓
Verification
↓
Compression Report

---

## Folder Structure

Dynamic-File-Compression-Utility/

├── input_files/

├── compressed_files/

├── decompressed_files/

├── src/

├── outputs/

├── images/

├── docs/

├── README.md

├── requirements.txt

├── .gitignore

└── main.py

---

## Sample Results

Compression Ratio Achieved: 55.93%

The project successfully compressed and decompressed the input file without data loss.

---

## Screenshots

* Project Structure
* Input File
* Frequency Table
* Min Heap Output
* Huffman Tree Creation
* Huffman Codes
* Compression Output
* Decompression Output
* Compression Report

---

## Learning Outcomes

Through this project I learned:

* Huffman Coding
* Tree Traversal
* Priority Queues
* Greedy Algorithms
* File Handling
* Compression Techniques
* Real-world Application of DSA

---

## Future Improvements

* Binary File Compression
* Folder Compression
* GUI Version
* Compression Analytics Dashboard
* Support for Multiple File Types

---

## Author

Dhiya Fathima
