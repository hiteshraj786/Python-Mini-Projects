from pikepdf import Pdf,Name,PdfImage

old_pdf = Pdf.open("ML.pdf")

page_1 = old_pdf.pages[0]
print(list(page_1.images.keys()))  # ['/Im0', '/Im1', '/Im2']

# raw_image = page_1.images['/Im2']
# pdf_image = PdfImage(raw_image)

# pdf_image.extract_to(fileprefix="test1")


# raw_image = page_1.images['/Im1']
# pdf_image = PdfImage(raw_image)

# pdf_image.extract_to(fileprefix="test2")


raw_image = page_1.images['/Im0']
pdf_image = PdfImage(raw_image)

pdf_image.extract_to(fileprefix="test0")