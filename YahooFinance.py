import requests


class Equity:
    __Symbol__ = ""
    Price = 0.0
    Name = ""

    def __init__(self, symbol):
        self.__Symbol__ = symbol
        

    def DownloadSummary(self):
        if (self.__Symbol__ == ""):
            raise Exception("Symbol was blank.")

        resp = requests.get("https://finance.yahoo.com/quote/" + self.__Symbol__)
        web = resp.text

        #Get price
        loc1 = web.find("Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D")
        loc1= web.find(">", loc1)
        loc2 = web.find("<", loc1 + 1)
        s = float(web[loc1+1:loc2])
        self.price = s


        loc1 = web.find("D(ib) Fz(16px) Lh(18px)")
        loc1 = web.find(">", loc1)
        loc2 = web.find("<", loc1 +1)
        name = web[loc1+1:loc2].replace("&amp;", "&").replace("&#x27;", "'")
        loc1 = name.find("-")
        self.Name = name[loc1+2:]

        

e = Equity("INTC")
e.DownloadSummary()
print(e.Name)