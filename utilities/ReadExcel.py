import pandas


class ReadExcelData:
    """ by using this class we can create a list of dict for each row with headers"""
    def __init__(self, file_location=None, sheet_name=None):
        self.path = file_location
        self.sheet_name = sheet_name

    def get_data(self):
        raw_data = pandas.read_excel(io=self.path, sheet_name=self.sheet_name, header=0, dtype='str')
        headers = list(raw_data.head())
        headers_size = len(headers)
        rows, columns = raw_data.shape
        # print(rows, columns)
        total_rows = []
        for row in range(rows):
            row_data = []
            for column in range(columns):
                cell_value = raw_data.iat[row, column]
                # print(cell_value)
                row_data.append(cell_value)
            result = dict(zip(headers, row_data))
            total_rows.append(result)
        # print(total_rows)
        return total_rows
