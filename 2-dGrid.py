import pandas as pd

def getTableDataSorted(url):
    tableData = pd.read_html(url, header=0, flavor='bs4')
    return tableData[0].sort_values(by=["y-coordinate","x-coordinate"], ascending=[False, True], ignore_index=True)


def printData(tableData):
    xco = tableData['x-coordinate']
    yco = tableData['y-coordinate']
    char = tableData['Character']

    for i in range(0, len(yco)):
        if (i != 0) and (xco[i] - xco[i - 1] != 1):
            print(" " * int((xco[i]) - (xco[i - 1]) - 1), end='')
        if (i !=0) and (yco[i] != (yco[i - 1])):
            print('\r')
        print (char[i], end='')

tableData = getTableDataSorted("https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub")
printData(tableData)