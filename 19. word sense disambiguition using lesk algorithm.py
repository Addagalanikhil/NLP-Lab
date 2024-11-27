from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
import nltk
nltk.download("wordnet")
nltk.download("omw-1.4")

# Input sentence
sentence = "I went to the bank to deposit money."

# Target word
word = "bank"

# Perform Lesk algorithm
sense = lesk(sentence.split(), word)
print(f"Word Sense for '{word}': {sense.name()} - {sense.definition()}")
