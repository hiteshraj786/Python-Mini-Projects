import pikepdf

oil_pdf = pikepdf.Pdf.open("timeTable.pdf")
no_extr = pikepdf.Permissions(extract=False)

oil_pdf.save("new.pdf",
             encryption=pikepdf.Encryption(user="123abc",
                                           owner="rajpurohit",
                                           allow = no_extr))