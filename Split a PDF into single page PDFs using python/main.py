import pikepdf

old_pdf = pikepdf.Pdf.open("FOT.pdf")

for n ,pag_can in enumerate(old_pdf.pages):
    new_pdf = pikepdf.Pdf.new()
    new_pdf.pages.append(pag_can)
    name = "test"+str(n)+".pdf"
    new_pdf.save(name)

