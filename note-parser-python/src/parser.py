import spacy

NLP = spacy.load("en_core_web_sm")

def parse_line_by_line(notes):
    expressions = []
    for line in notes.splitlines():
        if not len(line.split()) == 0:
            expressions.append(line)
    return expressions
    
def parse_sentences(notes):
    expressions = []
    doc = NLP(notes)
    doc_json = doc.to_json()
    sents = doc_json["sents"]
    text = doc_json["text"]
    for s in sents:
        start = s["start"]
        end = s["end"]
        sent_string = ""
        while start < end:
            sent_string = sent_string + text[start]
            start = start + 1
        expressions.append(sent_string)
    return expressions
        

def parse_lists(notes):
    expressions = []
    text = ""
    next_is_expression_end = False
    for i, line in enumerate(notes.splitlines()):
        if len(line.split()) == 0:
            continue
        if "\t" in line: 
            text = text + "\n" + line
        if "\t" not in line and next_is_expression_end:
            expressions.append(text)
            text = ""
            next_is_expression_end = False
        if "\t" not in line and not next_is_expression_end:
            text = text + line
            next_is_expression_end = True
        if i == len(notes.splitlines()) - 1 and len(text.split()) != 0:
            expressions.append(text)
    return expressions

def parse_categories(notes):
    expressions = []
    text = ""
    next_is_expression_end = False
    for line in notes.splitlines():
        if len(line.split()) == 0:
            continue
        if "\t" not in line:
            expressions.append(line)
        if "\t" in line and line.count("\t") == 1 and next_is_expression_end:
            expressions.append(text)
            text = ""
            next_is_expression_end = False
        if "\t" in line and line.count("\t") == 1 and not next_is_expression_end:
            text = text + "\n" + line
            next_is_expression_end = True
        if "\t" in line and line.count("\t") > 1:
            text = text + "\n" + line
        return expressions

def construct_docs(expressions):
    docs = []
    for e in expressions:
        docs.append(NLP(e))
    return docs
        
def generate_flashcards(expressions):
    cards = []
    return cards
                
file = open("notes.txt", "r")
notes = ""
for line in file:
   notes = notes + str(line)
expressions = parse_sentences(notes)
# print(expressions)
for e in expressions:
    print(e)
    print("~~~~~")
# docs = construct_docs(expressions)



