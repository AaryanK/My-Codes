from torch import layout
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

fp = open('download_papers/maths1.pdf', 'rb')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)



for i in PDFPage.get_pages(fp):
    interpreter.process_page(i)
    layout = device.get_result()
    for element in layout:
        print(element.mediaBox.getUpperRight_x(), element.mediaBox.getUpperRight_y())
        if instanceof(element, LTTextBox):
            print(element.get_text())
