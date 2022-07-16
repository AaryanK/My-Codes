import requests
from bs4 import BeautifulSoup
# import json



headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://r2.buddhaair.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://r2.buddhaair.com/index.jsp',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
  'userId': 'NARLTV',
  'password': 'ak330599'
}



def re_login(s):
    headers_re = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://r2.buddhaair.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://r2.buddhaair.com/u4OnlineReservation/main.jsp',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    data_re = {
    'reconfirmusr': 'NARLTV',
    'reconfirmpwd': 'ak330599',
    'confpwd': 'Confirm'
    }

    res = s.post('http://r2.buddhaair.com/u4OnlineReservation/rechkpwd.jsp', headers=headers_re, data=data_re, verify=False)
    res = s.get('http://r2.buddhaair.com/u4OnlineReservation/module.jsp?yourCurSessionId=UnitedSolutions')
    return s

def Login():
    s = requests.Session()
    res = s.post('http://r2.buddhaair.com/Home/login.jsp', headers=headers, data=data, verify=False)
    res = s.get('http://r2.buddhaair.com/u4OnlineReservation/module.jsp?yourCurSessionId=UnitedSolutions')
    
    return s


def Search(session,ddd,mmm,yyy,fromsector,tosector):
    headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://r2.buddhaair.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://r2.buddhaair.com/u4OnlineReservation/left.jsp',
    'Accept-Language': 'en-US,en;q=0.9',
}

    params = (
        ('viewopt', 'view'),
    )

    data = {
    'ddd': ddd,
    'mmm': mmm,
    'yyy': yyy,
    'fromsector': fromsector,
    'tosector': tosector,
    'searchby': 'PNR',
    'searchval': ''
    }
    response = session.post('http://r2.buddhaair.com/u4OnlineReservation/fdetail.jsp', headers=headers, params=params, data=data, verify=False)
    return response.content
    

class Fetch():
    def __init__(self,response):
        soup = BeautifulSoup(response,'html.parser')
        self.soup = soup
        self.js = {}
        self.flights={}
    def get_fares(self,fare="NPR"):
        fares = self.soup.find(id="fare")
        trs = fares.find_all('tr')
        i = trs[4]
        a = i.find_all(['tr','td'])
        SECTOR = a[1].get_text()
        # print(SECTOR)
        if "BHR" in SECTOR or "JKR" in SECTOR or "SKH" in SECTOR or "SKH" in SECTOR or "TMI" in SECTOR:
            for i in trs[4:7]:
                a = i.find_all(['tr','td'])
                a = a[1:]
                self.js['SECTOR'] = a[0].get_text()
                self.js[a[1].get_text()]=a[6].get_text()

        elif "SIF" in SECTOR:
            for i in trs[4:6]:
                a = i.find_all(['tr','td'])
                a = a[1:]
                self.js['SECTOR'] = a[0].get_text()
                # print(a[6].get_text())
                self.js[a[1].get_text()]=a[6].get_text()
        else:
            for i in trs[4:10]:
                a = i.find_all(['tr','td'])
                a = a[1:]
                self.js['SECTOR'] = a[0].get_text()
                self.js[a[1].get_text()]=a[6].get_text()
                # if fare == "USD":
                    # self.js["TOTAL_PRICE"] = a[11].get_text()
                # elif fare == "NPR":
                    # self.js["TOTAL_PRICE"] = a[6].get_text()

        return self.js

    def get_flight_and_seats(self):
        flights = self.soup.find_all(attrs={'class':'viewy'})
        for i in flights:
            j = i.a.find_all("td")
            # print(j)
            self.flights[j[2].get_text()] = {}
            try:
                self.flights[j[2].get_text()]["Y"]={"Number of seats available" : j[3].get_text(),"Unit Price":self.get_fares()["Y"]}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["A"]={"Number of seats available" : j[4].get_text(),"Unit Price":self.get_fares()["A"]}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["B"]={"Number of seats available" : j[5].get_text(),"Unit Price":self.get_fares()["B"]}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["D"]={"Number of seats available" : j[6].get_text(),"Unit Price":self.get_fares()["D"]}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["C"]={"Number of seats available" : j[7].get_text(),"Unit Price":self.get_fares()["C"]}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["E"]={"Number of seats available" : j[8].get_text(),"Unit Price":self.get_fares()["E"]}
            except:
                pass
        return self.flights



desrs = ["BDP","BHR","BIR","BWA","CCU","DHI","JKR","KEP","MTN","PKR","RJB","SIF","SKH","TMI","KTM"]
FROM = ["BDP","BHR","BIR","BWA","CCU","DHI","JKR","KEP","MTN","PKR","RJB","SIF","SKH","TMI","KTM"]


session = re_login(Login())

# for i in desrs:
#     try:
#         results = Search(session,'4','OCT','2021','KTM','SIF')

#         f = Fetch(results)
#         json = f.get_flight_and_seats()
#     except:
#         print(f"Error found at {i}")

results = Search(session,'05','OCT','2021','KTM','SIF')
f = Fetch(results)
json = f.get_flight_and_seats()
print(json)