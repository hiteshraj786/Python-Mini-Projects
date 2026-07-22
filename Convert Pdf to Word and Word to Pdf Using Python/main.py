
# # 🐍🐍 PDF To DOCX 🐍🐍

# from pdf2docx import Converter


# old_pdf = "ML.pdf"
# new_doc = "new.docx"


# obj =  Converter(old_pdf)
# obj.convert(new_doc) 

# obj.close()





# 🐍🐍 DOCX To PDF 🐍🐍

from docx2pdf import convert

convert("new.docx","new.pdf")
