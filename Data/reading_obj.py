
import xlrd
from Library.config import Config

class ReadExcel:

    def read_test_data(self):
        wb = xlrd.open_workbook(Config.TESTDATA_PATH)
        ws = wb.sheet_by_name(Config.Data_sheet)
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = []

        for row in rows:
            data.append((row[0].value,row[1].value,row[2].value,row[3].value,row[4].value,row[5].value,row[6].value))

        return data

    def read_locator(self, sheetname):
        wb = xlrd.open_workbook(Config.LOCATORS_PATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        dict_1 = {}
        for row in rows:
            dict_1[row[0].value] = (row[1].value ,row[2].value)
        return dict_1


# r = ReadExcel()
# data = r.read_test_data()
# print(data)
# # print(r.read_locator(Config.locator_sheet))
#
#





