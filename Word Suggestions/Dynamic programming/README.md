# 📝 Augmented Levenshtein Distance Algorithm

This code calculates the **augmented Levenshtein distance**, which determines:
- 🧮 The **minimum number of operations** required to transform a source string into a target string.
- 🛤️ The **sequence of operations (path)** to achieve this transformation.

## 📥 Input
- Two strings: `source` and `target`.

## 📤 Output
1. **Distance**: The minimum edit distance.
2. **Path**: A step-by-step transformation showing the required operations.

## 🌟 Example
For:
- **Source**: `'leda'`
- **Target**: `'deal'`

### Result:
- **Distance**: `3` 🧮
- **Path**: 
  - `['SUB(l->d)', 'INS(e)', 'MATCH(d)', 'MATCH(a)']` 🛤️
