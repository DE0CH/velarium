import pdf2image
import os
from django.contrib.staticfiles.storage import staticfiles_storage
import re
import logging
import uuid
import urllib.request
import textract
import string

def pdf_to_png_and_save(paper):
    # noinspection PyBroadException
    try:
        paper.pdf.seek(0, 0)
        pdf_byte = paper.pdf.read()
        image = pdf2image.convert_from_bytes(pdf_byte, last_page=1, dpi=100)[0]
        png_name = str(uuid.uuid4())
        image.save(png_name, 'PNG')
        with open(png_name, 'rb') as f:
            paper.png.save(os.path.basename(paper.pdf.name).replace('.pdf', '') + '.png', f)
        os.remove(png_name)
        paper.pdf.close()
    except:
        logging.exception('exception occurred converting pdf to png')
        with open(staticfiles_storage.path('failed/failed.png'), 'rb') as f:
            paper.png.save('failed.png', f)


def get_text(paper):
    id1 = str(uuid.uuid4())
    _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
    paper.pdf.seek(0, 0)
    with open(id1, 'wb') as of:
        of.write(paper.pdf.read())
    paper.pdf.close()
    text = textract.process(id1, extension='pdf').decode('utf-8')
    os.remove(id1)
    # Replace all white spaces with space: https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
    # Strip punctuation: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    return _RE_COMBINE_WHITESPACE.sub(" ", text).lower().translate(str.maketrans('', '', string.punctuation))



