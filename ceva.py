import requests
import csv

class StockItem(object):
    def __init__(self, open, high, close, volume):
        self.open = open
        self.high = high
        self.close = close
        self.volume = volume

    def get_open(self):
        return self.open

    def get_high(self):
        return self.high

    def get_close(self):
        return self.close

    def get_volume(self):
        return self.volume

    def __repr__(self):
        return "StockItem(%s, %s, %s, %s)" % (self.open, self.high, self.close, self.volume)

    def __eq__(self, other):
        if isinstance(other, StockItem):
            return ((self.open == other.open) and (self.high == other.high) and (self.close == other.close) and (self.volume == other.volume))
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())

class GetStockFinance(object):

    def __init__(self, url, stockindex):
        self.url = url
        self.stockindex = stockindex

    def get_stock_finance(self):
        download = requests.get(self.url+self.stockindex+'.csv')
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return list(cr)

    def get_stock_finance_return_set(self, filename):
        with open(filename, 'r') as csv_file:
            readCSV = csv.reader(csv_file)
            t = set()
            for i in readCSV:
                if len(i) != 0:
                    t.add(StockItem(i[1], i[2], i[3], i[4]))
        return t
class WriteToCsv(object):

    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, continut):
        with open(self.filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(continut)

    def read_from_csv(self, filename):
        with open(filename, 'r') as csv_file:
            readCSV = csv.reader(csv_file)
            t = set()
            for i in readCSV:
                if len(i) != 0:
                    t.add(StockItem(i[1], i[2], i[3], i[4]))
        return t


a = GetStockFinance('https://www.quandl.com/api/v3/datasets/WIKI/','AAPL')
#csv_de_scris = a.get_stock_finance()
y = a.get_stock_finance_return_set('copie.csv')
b = WriteToCsv('test.csv')
z = b.read_from_csv('test.csv')
c = y.difference(z)
d = z.difference(y)
for i in c:
    print(i.get_open())
for i in d:
    print(i.get_open())
#b = WriteToCsv('test.csv')
#b.write_to_csv(csv_de_scris)
