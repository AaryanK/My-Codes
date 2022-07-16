from pdfminer.layout import *
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import PyPDF2
import os


def check_question(x_coordinates):
    pass

def check_number(string):
    try:
        string = string.split()[0]
        string = int(string)
        return string
    except:
        return ''

file = 'download_papers/maths1.pdf'
for i in os.listdir('questions'):
    os.remove(f'questions/{i}')
document = open(file, 'rb')
#Create resource manager
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
p = PyPDF2.PdfFileReader(file)
pages = list(PDFPage.get_pages(document))

count = 1
for page in pages:
    pag = p.getPage(pages.index(page))
    
    this_page = []
    print(f'Processing page {pages.index(page)+1}')
    interpreter.process_page(page)
    # receive the LTPage object for the page.
    layout = device.get_result()
    for element in layout:
        if isinstance(element, LTContainer):
            if round(element.bbox[0]) == 49 or round(element.bbox[0]) == 50 or round(element.bbox[0]) == 48: 
               if isinstance(element, LTText):
                   text = element.get_text()
                   num = check_number(text)
                   if num != '':
                    # output = PyPDF2.PdfFileWriter()
                    # pag.cropBox[1],pag.cropBox[3] = element.bbox[1],element.bbox[3]
                    # output.addPage(pag)
                    
                    # with open(f"{num}.pdf", "wb") as out_f:
                    #     output.write(out_f)
                    print(num,element.bbox)
                    this_page.append(element.bbox)
    bboxes = []
    for i in range(len(this_page)):
        print(this_page.index(this_page[i]))
        if this_page[i] !=this_page[-1]:
            bbox = (pag.cropBox[0],this_page[i+1][-1],pag.cropBox[2],this_page[i][-1])
        else:
            bbox = (pag.cropBox[0],0,pag.cropBox[2],this_page[i][-1])
        bboxes.append(bbox)
    for i in bboxes:
        output = PyPDF2.PdfFileWriter()
        ul,ur,ll,lr = (i[0],i[3]+1),(i[2],i[3]+1),(i[0],i[1]),(i[2],i[1])
        pag.cropBox.upperLeft,pag.cropBox.upperRight,pag.cropBox.lowerLeft,pag.cropBox.lowerRight = ul,ur,ll,lr
        output.addPage(pag)
        

        

        with open(f"questions/{count}.pdf", "wb") as out_f:
            output.write(out_f)
            count+=1
