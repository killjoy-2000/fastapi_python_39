# import pandas as pd

# df = pd.read_excel("test_xl_py.xlsx")
# print(df)


import openpyxl

wb = openpyxl.load_workbook("test_xl_py.xlsx")
# print(wb.sheetnames)
# sheet = wb["Sheet1"]
sheet = wb["Sheet1"]
print(sheet.title)
print(sheet["A1"].value)

# for row in sheet.iter_rows(values_only=True):
#     for cell in row:
#         print(cell)

# data_to_put = {
#     "A" : "test",
#     "B" : "test2",
#     "C" : "test3"

# }

# sheet.append(data_to_put)
# wb.save("test_xl_py.xlsx")


wb.close()
