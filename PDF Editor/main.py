import pikepdf

old_pdf = pikepdf.Pdf.open("demo.pdf")

# reverse pdf 
# old_pdf.pages.reverse()
# old_pdf.save("rev_new.pdf")


# delete pages
# del old_pdf.pages[1:3]
# old_pdf.save("del_new.pdf")


old_pdf.pages[4] = old_pdf.pages[0]
old_pdf.save("rep_new.pdf")
