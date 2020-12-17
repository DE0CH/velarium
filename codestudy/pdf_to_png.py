import pdf2image
import uuid
import os
from django.contrib.staticfiles.storage import staticfiles_storage
from traceback import print_exc

def pdf_to_png(paper, pdf):
    # noinspection PyBroadException
    pdf_byte = pdf.read()
    try:
        image = pdf2image.convert_from_bytes(pdf_byte, last_page=1, dpi=100)[0]
        png_name = str(uuid.uuid4())
        image.save(png_name, 'PNG')
        with open(png_name, 'rb') as f:
            paper.png.save(os.path.basename(pdf.name).replace('.pdf', '') + '.png', f)
        os.remove(png_name)
        print('converted')
    except:
        print_exc()
        print('error')
        with open(staticfiles_storage.path('failed/failed.png'), 'rb') as f:
            paper.png.save('failed.png', f)
    print('exited')
