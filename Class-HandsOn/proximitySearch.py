import nltk
from nltk.text import Text

# Create a Text object from a list of tokens
tokens = nltk.word_tokenize("This is a test sentence. It is used to demonstrate proximity search.")
text = Text(tokens)

# Create a ConcordanceIndex object
index = nltk.ConcordanceIndex(text.tokens, key=lambda s: s.lower())

# Search for the word "test" within 5 words of the word "sentence"
matches = index.find_concordance("sentence", 5)
print(matches)
