import pikepdf

 
my_pdf = pikepdf.Pdf.open("timeTable.pdf")

for i in my_pdf.pages:
    i.Rotate = 180
my_pdf.save("new_pdf.pdf")




















