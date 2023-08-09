import openpyxl

try:
    wb = openpyxl.load_workbook("test_xl_py.xlsx")
    sheet = wb["Sheet2"]
    def check_sts(ip):
        # print(ip)
        try:
            search_value = ip
            found_cells = []
            col = sheet["A"]
            # for row in sheet.iter_rows():
            #     for cell in row:
            #         # if cell != search_value:
            #         #     s = "data inserted"
            #         #     
            #         #     sheet.append(put_data)
            #         #     wb.save("log.xlsx")
            #         #     return s
            #         if cell.value == search_value:
            #             s = "data found"
            #             found_cells.append(row)
            #             return s
            for cell in col:
                if cell.value == search_value:
                    # cell.value = None
                    # sheet.delete_rows(cell.row, 1)
                    # wb.save("test_xl_py.xlsx")
                    # if row[1].value == "T":
                    #     row[1].value = "F"
                    return True
                # else:
            put_data = {
                    "A": search_value,
                    "B" : "T",
                    "C" : "T",
                }
            sheet.append(put_data)
            wb.save("test_xl_py.xlsx")
            return False
        except Exception as e:
            print(str(e))
            return str(e)

        # return "sec"
    # print(sheet["A2"].value)


except Exception as e:
    print(str(e))

finally:
    wb.close()

