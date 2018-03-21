import openpyxl
wb=openpyxl.Workbook()
sheet=wb.get_active_sheet
# sheet.title='福州晋安房价'
sheet['A2']='HELLO WORLD!'
wb.save('c:\\1.xlsx')
