import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        contor = 0
        file = open("Paragrafe.txt", "w", encoding='utf-8')
        a=text.split("  ")

        for paragraph in a :
            print(paragraph)
            b=paragraph.split()
            if(b.count("este")>=2):
                print(b.count('pe'))
            if(b.count("pe")==2):
                 file.write(paragraph)
                 contor += 1


    return text

if __name__ == '__main__':
    print(extract_text_from_pdf('romania.pdf'))