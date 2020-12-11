from docx.opc.constants import RELATIONSHIP_TYPE as RT

def docx_replace_regex(doc_obj, regex, replace):
    for p in doc_obj.paragraphs:
        if regex.search(p.text):
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if regex.search(inline[i].text):
                    text = regex.sub(replace, inline[i].text)
                    inline[i].text = text

    for table in doc_obj.tables:
        for row in table.rows:
            for cell in row.cells:
                docx_replace_regex(cell, regex, replace)

    rels = doc_obj.part.rels

    for rel in rels:
        if rels[rel].reltype == RT.HYPERLINK:
            # print("\n Origianl link id -", rel, "with detected URL: ", rels[rel]._target)
            new_url = replace
            rels[rel]._target = new_url

def redacted_string(input):
    print(input.__repr__())
    length = len(input.__repr__())
    # print("input string is"+ str(input.__str__()))
    return '*' * length