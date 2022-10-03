from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = 'qq'

ws.append([123,456,789,0])

wb.save('../static/excels/new_excel.xlsx')