# BBC Dataset for Text Classification

The **BBC dataset** contains text samples categorized into five distinct classes: Business, Entertainment, Politics, Sport, and Tech. This dataset is commonly used for training and evaluating text classification models, such as the Naive Bayes classifier.

---

## Dataset Overview

- **Source**: Extracted from BBC news articles.
- **Format**: CSV file (`bbc_data.csv`).
- **Total Samples**: 2,225
- **Columns**:
  - `data`: The text content of the news articles.
  - `labels`: The category or class to which the article belongs.

---

## Classes and Distribution

| Class          | Description                           | Number of Samples |
|----------------|---------------------------------------|-------------------|
| **Business**   | Articles related to business news.    | ~450              |
| **Entertainment** | Articles related to movies, music, and celebrities. | ~400 |
| **Politics**   | Articles about politics and government affairs. | ~350 |
| **Sport**      | Articles covering sports events.      | ~500              |
| **Tech**       | Articles about technology and gadgets.| ~525              |

---

## File Format

The dataset is stored in a **CSV (Comma-Separated Values)** format with the following columns:

| Column Name | Data Type | Description                                      |
|-------------|-----------|--------------------------------------------------|
| `data`      | `string`  | The content of the news article.                |
| `labels`    | `string`  | The category label for the article.             |

### Example Rows
| data                                  | labels       |
|---------------------------------------|--------------|
| "Apple's new iPhone hits the market." | tech         |
| "Manchester United wins the cup."    | sport        |
| "Stock markets see record gains."     | business     |

---
- **GitHub**: [Aym4n33](https://github.com/Aym4n33)


