class Node:
    def __init__(self):
        self.children = dict()
        self.end_of_the_word = False
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self,word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = Node()
            current_node = current_node.children[c]
        current_node.end_of_the_word = True
    def search(self,word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return True
    def _levenshtein_distance(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j  
                elif j == 0:
                    dp[i][j] = i  
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])  

        return dp[m][n]
    def _dfs_suggest(self, node, target, current_word, max_distance, suggestions):
        current_distance = self._levenshtein_distance(target, current_word)
        
        if current_distance > max_distance:
            return  

        if node.end_of_the_word and current_distance <= max_distance:
            suggestions.append((current_word, current_distance))  

        for char, child_node in node.children.items():
            self._dfs_suggest(child_node, target, current_word + char, max_distance, suggestions)
    def suggestion(self,word,max_distance):
        suggestions_with_scores = []
        self._dfs_suggest(self.root, word, "", max_distance, suggestions_with_scores)
        sorted_suggestions = sorted(suggestions_with_scores, key=lambda x: x[1])
        return [word for word, _ in sorted_suggestions]
    

trie = Trie()

file_path = r"C:\Users\Aymane\Desktop\All\projets\NLP\misspelled\american-english.txt" 

with open(file_path, "r") as file:
    for line in file:
        word = line.strip()  
        if word:  
            trie.insert(word)

print("Trie loaded with dictionary words.")
print("Type 'i quit' to exit.")

while True:
    misspelled_word = input("Enter a misspelled word: ").strip()
    if misspelled_word.lower() == 'i quit':
        print("Goodbye!")
        break

    try:
        max_distance = int(input("Enter maximum Levenshtein distance (At least equal to the length of the word): ").strip())
    except ValueError:
        print("Please enter a valid number for maximum distance.")
        continue

    suggestions = trie.suggestion(misspelled_word, max_distance)
    print("Suggestions:", suggestions[:20])