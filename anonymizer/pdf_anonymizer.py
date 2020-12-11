import numpy
from PIL import Image
import re
import cv2
from anonymizer import generate_filename
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import pytesseract


# images = convert_from_path('../resumev8.pdf', fmt="jpeg")

# i.save('../output.jpg', 'JPEG')

# print(pytesseract.image_to_string(Image.open('../output.jpg')))
# print(pytesseract.image_to_boxes(Image.open('../output.jpg')))


def convert_to_image(path):
    images = convert_from_path(path)

    return images

def anonymize(path, output, words):
    pages = convert_to_image(path)

    for j in pages:
        # img= cv2.imread(j)
        img = cv2.cvtColor(numpy.array(j), cv2.COLOR_RGB2BGR)

        d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        # print(d)
        n_boxes = len(d['level'])
        for i in range(n_boxes):
            for word in words:
                if word.lower() in d['text'][i].lower():
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), -1)

        # cv2.imshow('img', img)
        cv2.imwrite(output+".png", img)
        # cv2.waitKey(0)






