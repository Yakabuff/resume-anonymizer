# # parse(pdf_file, docx_file, start=0, end=1)
# content = []
# txt = docx2txt.process(docx_file)
# for x in txt.split():
#     content.append(x)
#
# clean_string = ' '.join(str(x) for x in content)
# print(clean_string)
#
# email_regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
#
# # email = re.findall('\S+@\S+', clean_string)
# email = re.findall(email_regex, clean_string)
# print(email)
# # images.save("img1.png", "png")
#

# class anonymize:
#     def __init__(self, fields):
#         self.field = fields
import os
import re
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT

from anonymizer import hyperlink_remover


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

def redacted_string(input)->str:
    print(input.__repr__())
    length = len(input.__repr__())
    # print("input string is"+ str(input.__str__()))
    return '*' * length

def anonymize(input, output, keywords):
    doc = Document(input)
    base = os.path.splitext(input)[0]
    os.rename(input, base+".zip")
    hyperlink_remover.remove_link(base + ".zip")
    os.rename(base+".zip", base + ".docx")
    for i in keywords:
        docx_replace_regex(doc, re.compile(i), redacted_string(i))
    doc.save(output);
    print("Done :)")


