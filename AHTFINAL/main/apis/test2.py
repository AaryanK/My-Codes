import requests
from bs4 import BeautifulSoup
# from requests import cookies


session = requests.Session()
c = session.get("http://shreeair.org/")
cookies = session.cookies.get_dict()



headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://shreeair.org',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://shreeair.org/',
    'Accept-Language': 'en-US,en;q=0.9',
}


def login():
    data = {
    'ipAddress': 'IpAddress',
    'clientOs': '',
    'macAddress': 'CPUId',
    'macAddress1': 'NetworkId',
    'requestFrom': 'Direct',
    'userId': 'ANTUHI',
    'password': 'ak330599'
    }



    
    response = session.post('http://shreeair.org/Home/login.jsp', headers=headers, cookies=cookies, data=data, verify=False)
    
    # print(response.content)
    response = session.get('http://shreeair.org/SaOnlineReservation/loginagent.jsp', headers=headers, cookies=cookies, verify=False)

    return session


def relogin(s):
    data = {
    'reconfirmusr': 'ANTUHI',
    'reconfirmpwd': 'ak330599',
    'confpwd': 'Confirm'
    }

    response = s.post('http://shreeair.org/SaOnlineReservation/rechkpwd.jsp', headers=headers, cookies=cookies, data=data, verify=False)
    return s


def Search(session,ddd,mmm,yyy,fromsector,tosector):
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

    response = session.post('http://shreeair.org/SaOnlineReservation/fdetail.jsp', headers=headers, params=params, cookies=cookies, data=data, verify=False)
    return response.content




class Fetch():
    def __init__(self,response):
        soup = BeautifulSoup(response,'html.parser')
        self.response= response
        self.soup = soup
        self.js = {}
        self.flights={}
    def get_fares(self,fare="NPR"):
        fares = self.soup.find(id="fare")
        trs = fares.find_all('tr')
        for i in trs[3:9]:
            a = i.find_all(['tr','td'])
            a=a[1:]
            # print(a)
            self.js['SECTOR'] = a[0].get_text()
            self.js[a[1].get_text()]=a[6].get_text()
        return self.js

    def get_special_fares(self):
        soup = BeautifulSoup(self.response,'lxml')
        _class = soup.find_all(attrs={'class':'viewy'})
        _list=[]
        for i in _class:
            z = i.find_all("a")[0].get_text()
            print(z)
            j = i.find_all("td")[-1].get_text()
            print(j)
            if "Cls" in j:
                dict = {'Flight number': z, 'Class': j.split()[0][5], 'New Fare': j.split()[2]}
                _list.append(dict)
            # for (s,l) in z,j:
            #    flight_number =  s.get_text()
            #    if "Class" in l.get_text():
            #         offer_price=l.get_text()
            #         print(flight_number,offer_price)
        return _list
    
    def get_flight_and_seats(self):
        flights = self.soup.find_all(attrs={'class':'viewy'})
        for i in flights:
            j = i.a.find_all("td")
            self.flights[j[2].get_text()] = {}
            try:
                self.flights[j[2].get_text()]["H"]={"Flight no.":i.a.get_text()[:7],"Number of seats available" : j[3].get_text(),"Unit Price":self.get_fares()["H"],"Class":"H"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["I"]={"Flight no.":i.a.get_text()[:7],"Number of seats available" : j[4].get_text(),"Unit Price":self.get_fares()["I"],"Class":"I"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["B"]={"Flight no.":i.a.get_text()[:7],"Number of seats available" : j[5].get_text(),"Unit Price":self.get_fares()["B"],"Class":"B"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["E"]={"Flight no.":i.a.get_text()[:7],"Number of seats available" : j[6].get_text(),"Unit Price":self.get_fares()["E"],"Class":"E"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["S"]={"Flight no.":i.a.get_text()[:7],"Number of seats available" : j[7].get_text(),"Unit Price":self.get_fares()["S"],"Class":"S"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["T"]={"Flight no.":i.a.get_text()[:7],"Number of seats available" : j[8].get_text(),"Unit Price":self.get_fares()["T"],"Class":"T"}
            except:
                pass
        self.flights_list=[]
        for i in self.flights:
            for j in self.flights[i]:
                time= f"{i[0:2]}:{i[2:]}"
                dict = {"Flight no.":self.flights[i][j]["Flight no."],"Class":self.flights[i][j]["Class"],"Time":time,"Maximum_Seats":self.flights[i][j]["Number of seats available"],"Unit_Price":self.flights[i][j]["Unit Price"]}
                # print(dict)
                self.flights_list.append(dict)
        improvise = self.get_special_fares()
        for i in improvise:
            for j in self.flights_list:
                if i["Flight number"] == j["Flight no."]:
                    if i["Class"]==j["Class"]:
                        j["Unit_Price"]=i["New Fare"]
        self.flights_list={"Shree Air":self.flights_list}
        return self.flights_list
session = relogin(login())
results = Search(session,'14','OCT','2021','BDP','KTM')
print(Fetch(results).get_flight_and_seats())