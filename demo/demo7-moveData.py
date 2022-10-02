from openpyxl import Workbook, load_workbook

wb_url = '../static/excels/new_excel.xlsx'
wb = load_workbook(wb_url)
ws = wb.active

ws.move_range('B2:B2',rows=2)


wb.save(wb_url)