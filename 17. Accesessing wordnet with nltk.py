from nltk.corpus import wordnet as wn
import nltk
nltk.download("wordnet")
nltk.download("omw-1.4")

# Input word
word = "bank"

# Retrieve synsets
synsets = wn.synsets(word)
print(f"Synsets for '{word}':")
for synset in synsets:
    print(f"{synset.name()}: {synset.definition()}")

# Explore synonyms, antonyms, and examples for the first synset
if synsets:
    first_synset = synsets[0]
    print("\nExamples:", first_synset.examples())
    print("Synonyms:", [lemma.name() for lemma in first_synset.lemmas()])
    antonyms = [lemma.antonyms()[0].name() for lemma in first_synset.lemmas() if lemma.antonyms()]
    print("Antonyms:", antonyms)
