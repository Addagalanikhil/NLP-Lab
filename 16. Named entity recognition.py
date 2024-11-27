import spacy

# Load SpaCy's English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "John works at Google and lives in New York."

# Perform Named Entity Recognition
doc = nlp(text)

print("Named Entities:")
for entity in doc.ents:
    print(f"{entity.text} - {entity.label_} ({spacy.explain(entity.label_)})")
