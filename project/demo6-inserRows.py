from openpyxl import Workbook, load_workbook

wb_url = '../static/excels/new_excel.xlsx'
wb = load_workbook(wb_url)
ws = wb.active

# ws.insert_rows(5)
# ws.insert_cols(3)

# ws.delete_cols(3)
# ws.delete_rows(5)
# ws.insert_cols()

wb.save(wb_url)