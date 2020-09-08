import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Give it back! He pleaded.")
give_children = doc[0].children
print(doc[0].children)