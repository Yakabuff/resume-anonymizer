
import os
from docx import Document
import re
import timeit
from anonymizer import pdf_anonymizer
from anonymizer import hyperlink_remover
from anonymizer import generate_filename
from anonymizer import docx_anonymizer


def anonymize(input, output, keywords):

    if(os.path.splitext(input)[1]=='.docx'):
        doc = Document(input)
        base = os.path.splitext(input)[0]
        os.rename(input, base+".zip")
        hyperlink_remover.remove_link(base + ".zip")
        os.rename(base+".zip", base + ".docx")
        for i in keywords:
            docx_anonymizer.docx_replace_regex(doc, re.compile(i), docx_anonymizer.redacted_string(i))
        doc.save(output);
    elif(os.path.splitext(input)[1]=='.pdf'):
        print("pdf")
        pdf_anonymizer.anonymize(input, generate_filename.generate_filename(), keywords)
    else:
        print('unsupported format :(')

    print("Done :)")


