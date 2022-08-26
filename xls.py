import xlsxwriter
from tviy_clone_3 import array


def writer(parameter):
    book = xlsxwriter.Workbook(r"\\VM-WES\Перенаправление папок\andr.romanenko\Desktop\parser.xlsx")
    page = book.add_worksheet("Товары")

    row = 0
    column = 0

    page.set_column("A:A", 70)
    page.set_column("B:B", 20)
    page.set_column("C:C", 20)
    page.set_column("D:D", 50)
    page.set_column("E:E", 20)
    page.set_column("F:F", 50)

    for item in parameter:
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        row += 1

    book.close()


writer(array())