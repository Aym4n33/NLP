# Naive Bayes Text Classification

This project implements a **Naive Bayes classifier** for text classification, designed to predict the category of textual data. The model achieves an impressive accuracy of **97.30%** on the test set.

---

## Features

- **Text Preprocessing**: 
  - Converts text to lowercase.
  - Removes punctuation.
  - Tokenizes text using the `nltk` library.
- **Naive Bayes Model**:
  - Implements Laplace smoothing to handle unseen words in the test set.
  - Calculates prior probabilities for each class and likelihoods for each token.
- **Evaluation**:
  - Outputs precision, recall, F1-score, and accuracy for each class.
  - Generates detailed performance metrics using `sklearn`.

---

## Dataset

- The dataset contains text samples categorized into the following classes:
  - `business`
  - `entertainment`
  - `politics`
  - `sport`
  - `tech`

- **Train-Test Split**:
  - Training data: Used to calculate priors and likelihoods.
  - Test data: Evaluated for model metrics.

---

## Results

### Overall Accuracy
- The model achieves an accuracy of **97.30%**.

### Classification Report
| Class          | Precision | Recall | F1-Score | Support |
|----------------|-----------|--------|----------|---------|
| Business       | 98%       | 94%    | 96%      | 103     |
| Entertainment  | 100%      | 95%    | 98%      | 84      |
| Politics       | 93%       | 99%    | 96%      | 80      |
| Sport          | 100%      | 99%    | 99%      | 98      |
| Tech           | 95%       | 100%   | 98%      | 80      |

- **Macro Avg**: Precision = 97%, Recall = 97%, F1-Score = 97%
- **Weighted Avg**: Precision = 97%, Recall = 97%, F1-Score = 97%

---


## Usage

### Prerequisites
- Libraries: `pandas`, `nltk`, `sklearn`

- **GitHub**: [Aym4n33](https://github.com/Aym4n33)

