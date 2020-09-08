import spacy

NLP = spacy.load("en_core_web_sm")

#testing spacy apis 
notes = "The cell is the smallest unit of life that can perform all activities required for life. Cells share characteristics. They have Two main forms: Prokaryotic (no nucleus containing DNA)Eukaryotic (nucleus contains DNA) Chromosomes contain genetic material in the form of DNA. Genes are units of inheritance that transmit information from parents to offspring"
doc = NLP(notes)
doc_json = doc.to_json()
text = doc_json["text"]
sents = doc_json["sents"]
ents = doc_json["ents"]
cards = []
i = 1

print()
print("SENTENCES")

for s in sents:
    start = s["start"]
    end = s["end"]
    print("~~ Sentence " + str(i) + " ~~")
    sent_string = ""
    card = {"front": "", "back": ""}
    front = True
    while(start < end):
        sent_string = sent_string + text[start]
        start = start + 1
    print(sent_string)
    sent_doc = NLP(sent_string)
    index = 0
    for token in sent_doc:
        if front:
            if token.pos_ == "AUX" or token.pos_ == "VERB":
                card["front"] = card["front"] + token.text
                front = False
            else:
                card["front"] = card["front"] + token.text + " "
        else:
            card["back"] = card["back"] + token.text + " "
        index = index + 1
    print(card)
    print("----------")
    i = i + 1
