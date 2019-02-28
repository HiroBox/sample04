import os
import openpyxl

os.chdir("C:/Users/nakamura/Documents/EBX/Python")
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "worksheettitle"

wb.save('example.xlsx')


