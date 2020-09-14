import spacy

NLP = spacy.load("en_core_web_sm")
#len(token.text.split()) == 0 and len(token.text) > 1

def parse_categories(notes):
    expressions = []
    text = ""
    next_is_expression_end = False
    next_is_category_end = False
    for line in notes.splitlines():
        if len(line.split()) == 0:
            continue
        if "\t" not in line and next_is_category_end:
            expressions.append(text)
            text = ""
            next_is_category_end = False
        if "\t" not in line and not next_is_category_end:
            text = text + line
            next_is_category_end = True
        if "\t" in line and line.count("\t") == 1 and next_is_expression_end:
            #text = text + "\n" + line
            expressions.append(text)
            text = ""
            next_is_expression_end = False
        if "\t" in line and line.count("\t") == 1 and not next_is_expression_end:
            text = text + "\n" + line
            next_is_expression_end = True
        if "\t" in line and line.count("\t") > 1:
            text = text + "\n" + line
    for e in expressions:
        print(e)
        print("~~~~~")
                
file = open("notes.txt", "r")
notes = ""
for line in file:
   notes = notes + str(line)
doc = NLP(notes)
print("----------")
parse_categories(notes)
# for token in doc:
    # print(token, " -- ", token.pos_)
# doc_json = doc.to_json()
# #print(doc_json)
# text = doc_json["text"]
# sents = doc_json["sents"]
# ents = doc_json["ents"]
# cards = []
# i = 1



# print()
# print("SENTENCES")

# for s in sents:
    # start = s["start"]
    # end = s["end"]
    # print("~~ Sentence " + str(i) + " ~~")
    # sent_string = ""
    # card = {"front": "", "back": ""}
    # front = True
    # while(start < end):
        # sent_string = sent_string + text[start]
        # start = start + 1
    # print(sent_string)
    # sent_doc = NLP(sent_string)
    # index = 0
    # for token in sent_doc:
        # print(token, " - ", token.pos_)
        # if front:
            # if token.pos_ == "AUX" or token.pos_ == "VERB":
                # card["front"] = card["front"] + token.text
                # front = False
            # else:
                # card["front"] = card["front"] + token.text + " "
        # else:
            # card["back"] = card["back"] + token.text + " "
        # index = index + 1
    # print(card)
    # print("----------")
    # i = i + 1
