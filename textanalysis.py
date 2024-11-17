from mediawiki import MediaWiki
from collections import Counter
import re
import nltk
from textblob import TextBlob
from thefuzz import fuzz

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Initialize MediaWiki
wikipedia = MediaWiki()

# Fetch the Babson College page
babson = wikipedia.page("Babson College")

# Get the content
content = babson.content

print(f"Title: {babson.title}")
print(f"Content length: {len(content)} characters")

# Remove punctuation and convert to lowercase
words = re.findall(r'\w+', content.lower())

# Count word frequencies
word_freq = Counter(words)

# Print the 10 most common words
print("\n## Most Common Words")
for word, count in word_freq.most_common(10):
    print(f"{word}: {count}")

# Sentence analysis
sentences = nltk.sent_tokenize(content)

print(f"\n## Sentence Analysis")
print(f"Total sentences: {len(sentences)}")
print(f"Average sentence length: {sum(len(s.split()) for s in sentences) / len(sentences):.2f} words")

# Named Entity Recognition
try:
    def extract_entities(text):
        chunks = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text)))
        entities = []
        for chunk in chunks:
            if hasattr(chunk, 'label'):
                entities.append(' '.join(c[0] for c in chunk))
        return entities

    all_entities = extract_entities(content)
    entity_freq = Counter(all_entities)

    print("\n## Top Named Entities")
    for entity, count in entity_freq.most_common(10):
        print(f"{entity}: {count}")
except Exception as e:
    print(f"\n## Named Entity Recognition failed: {str(e)}")
    print("Skipping Named Entity Recognition.")

# Sentiment Analysis
blob = TextBlob(content)
sentiment = blob.sentiment

print("\n## Sentiment Analysis")
print(f"Polarity: {sentiment.polarity:.2f}")
print(f"Subjectivity: {sentiment.subjectivity:.2f}")

# Similarity Analysis
print("\n## Similarity Analysis")
print(f"Similarity ratio: {fuzz.ratio('Babson College', 'Babson University')}")
print(f"Partial ratio: {fuzz.partial_ratio('Babson College', 'Babson University')}")
print(f"Token sort ratio: {fuzz.token_sort_ratio('Babson College', 'College Babson')}")