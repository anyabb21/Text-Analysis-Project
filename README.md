# Text-Analysis-Project

Please read the [instructions](instructions.md).

# Text Analysis of Babson College Wikipedia Page

## Project Overview

This project focuses on analyzing the Wikipedia page for Babson College using various natural language processing (NLP) techniques. The main data source is the MediaWiki API, which allows us to fetch the text content of the page. The analysis includes word frequency counts, sentence structure analysis, named entity recognition, and sentiment analysis. The goal was to extract meaningful insights from the text and enhance my understanding of NLP methods.

## Implementation

The implementation is done in Python, utilizing libraries such as `mediawiki`, `nltk`, `textblob`, and `thefuzz`. The architecture consists of several key components:

1. **Data Retrieval**: The `mediawiki` library is used to fetch the content of the Babson College Wikipedia page.
2. **Text Processing**: The text is cleaned and tokenized using regular expressions and NLTK.
3. **Analysis Modules**:
   - **Word Frequency Analysis**: This counts how often each word appears in the text.
   - **Sentence Analysis**: NLTK's sentence tokenizer breaks down the text into sentences and calculates their lengths.
   - **Named Entity Recognition**: NLTK's NE chunker identifies names and places within the text.
   - **Sentiment Analysis**: TextBlob analyzes the sentiment of the text to determine its overall positivity or negativity.
   - **Similarity Analysis**: TheFuzz library is used to compare strings for similarity.

A significant design decision was choosing between NLTK and spaCy for NLP tasks. I opted for NLTK due to its extensive documentation and built-in resources, which were helpful for learning.

I also leveraged GenAI tools like Perplexity AI to troubleshoot issues related to NLTK resource downloads and to refine my implementation.

## Results

The analysis yielded several interesting findings:

1. **Most Common Words**:
   - The top words included "of" (55 occurrences), "the" (52), and "and" (50), which are common in English texts.
   - "Babson" appeared 22 times, emphasizing the focus on Babson College