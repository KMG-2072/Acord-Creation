import json

from PyPDF2 import PdfReader, PdfWriter
import pandas as pd
def read_acord(type):

    reader = PdfReader("Acord125.pdf")
    writer = PdfWriter()
    page= reader.pages[0]
    # fields = reader.get_fields()
    # field_names = [key.split(".")[-1] for key in fields.keys()]
    with open("Fields_Excel.txt",'r') as file:
        field_list = [field.strip() for field in file.read().split(",")]

    df = pd.DataFrame(columns=field_list)
    df.to_csv('input.csv',index='False')
    # writer.add_page(page)
    # writer.update_page_form_field_values(writer.pages[0] , {'Producer_FullName_A[0]':'Sterling Reserve'})
    # writer.update_page_form_field_values(writer.pages[0], {'Producer_ContactPerson_EmailAddress_A[0]': 'stertling.res@gmail.com'})
    # with open("auto.pdf",'wb') as file:
    #     writer.write(file)

read_acord('')
