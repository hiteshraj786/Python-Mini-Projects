from pdf2image import convert_from_path

old_pdf = convert_from_path("FOT.pdf",poppler_path=r'C:\Python Course\Python_Project\Convert Pdf to Image Using Python\poppler-24.08.0\Library\bin')


for i in range(len(old_pdf)):
    old_pdf[i].save("new"+str(i+1)+".jpg","JPEG")
