import openpyxl

wb = openpyxl.load_workbook("projects.xlsx")
ws = wb.active

print(ws)