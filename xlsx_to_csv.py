import csv
import openpyxl
import platform

def convert(filename, csvname):
    #filename = 'iris_data.xlsx'
    wb = openpyxl.load_workbook(filename)
    sheet = wb["Fisher's Iris Data"]
    #csvname = 'iris_data.csv'

    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open(csvname, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)

        for rowOfCellObjects in sheet['A1':'E151']:
            ls = []
            for cellObj in rowOfCellObjects:
                ls.append(cellObj.value)
            output_writer.writerow(ls)