# 📚 Misspelled Word Suggestions using Trie and Levenshtein Distance

This project implements a **misspelled word suggestion system** using a **Trie data structure** combined with **Levenshtein Distance** for approximate string matching. It reads a dictionary of valid words and suggests corrections for user-provided misspelled words within a specified maximum distance.

## 🛠️ How It Works

1. **Trie Data Structure**:
   - All words from a dictionary file are stored in a Trie.
   - Each word is broken down character by character and inserted into the Trie to enable efficient prefix-based searches.

2. **Levenshtein Distance**:
   - Used to calculate the "edit distance" between the user's input and each word in the Trie.
   - Edit distance includes:
     - Insertion
     - Deletion
     - Substitution of characters

3. **Approximate String Matching**:
   - Words in the Trie are compared against the input word.
   - Words within the specified maximum distance are returned as suggestions.

4. **Suggestions Ranking**:
   - Suggestions are sorted by their edit distance (from smallest to largest) to provide the most accurate corrections.

---

## 🎯 Features

- **Misspelled Word Detection**: 
  - Suggests corrections for words that may be misspelled.
  
- **Customizable Accuracy**:
  - Users can specify the maximum Levenshtein distance to control how "close" suggestions should be.

- **Efficient Search**:
  - The Trie structure enables efficient traversal and searching through a large dictionary.

---

## 🗂️ File Structure

- **Trie Class**:
  - Implements word insertion, search, and suggestion functionality.
  
- **Levenshtein Distance**:
  - Calculates the edit distance between two strings using dynamic programming.

- **DFS-Based Suggestions**:
  - Uses Depth-First Search (DFS) to traverse the Trie and find words within the acceptable distance.

- **Dictionary File**:
  - A text file (`american-english.txt`) containing valid words for the Trie.

---

## 🧑‍💻 How to Use

1. Place your dictionary file (e.g., `american-english.txt`) in the same directory as the script.
2. Run the script to load the Trie with dictionary words.
3. Enter a misspelled word and specify the maximum Levenshtein distance. Mke sure the maximum Levenshtein distance is at least equal to the length of the word.
4. View up to 20 suggestions ranked by edit distance.

---

## 🔍 Example Usage

### Input:
- Misspelled Word: `recieve`
- Max Distance: `7`

### Output:
['receive', 'relieve', 'believe', 'recede',  'recipe', 'recite', 'reeve', 'relieved', 'reliever', 'relieves', 'relive', 'reprieve', 'retrieve', 'revive', 'achieve', 'believed', 'believer', 'believes', 'besiege', 'Cecile']
