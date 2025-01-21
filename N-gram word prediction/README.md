# Word Prediction with N-Gram Models

This project implements a word prediction system using **n-gram language models**, with support for interpolation smoothing to improve predictions. The code processes a text corpus, calculates n-gram probabilities, and evaluates the model using common metrics.

## Features

- **Tokenization**: Preprocessing the text using the Punkt tokenizer (NLTK).
- **N-Gram Models**: Unigram, bigram, and trigram calculations.
- **Smoothing**: Interpolation smoothing for handling zero-probability n-grams.
- **Evaluation**:
  - **Intrinsic**: Using **Perplexity** to measure model performance.
  - **Extrinsic**: Based on the quality of word predictions.
- **Customizability**: Simple weight selection for interpolation.

## How It Works

1. **Data Preparation**:
   - Special markers are added to sentences for trigram modeling.
   - The dataset is split into training and test sets.

2. **Model Training**:
   - N-gram probabilities are computed.
   - Interpolation smoothing is applied for robust probability distribution.

3. **Evaluation**:
   - Perplexity is used to measure the model's uncertainty.
   - Predictions are evaluated against ground truth.

## Future changes:
- Include other smoothing methods like the conditional interpollation.
- Implement, train and test the BPE tokenizer.
- Implement the Expectation Maximisation algorithm and retrieve weights.
