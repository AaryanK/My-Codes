import requests
from bs4 import BeautifulSoup, FeatureNotFound

# import json



buddha_headers_1 = {
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

buddha_data_1 = {
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
    res = s.post('http://r2.buddhaair.com/Home/login.jsp', headers=buddha_headers_1,data=buddha_data_1, verify=False)
    res = s.get('http://r2.buddhaair.com/u4OnlineReservation/module.jsp?yourCurSessionId=UnitedSolutions')
    
    return s


def Search(session,ddd,mmm,yyy,fromsector,tosector):
    # self.sector = f'{fromsector}-{tosector}'
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
    def __init__(self,response,session):
        soup = BeautifulSoup(response,'html.parser')
        self.session = session
        self.response = response
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

        return self.js

    def get_special_fares(self):
        soup = BeautifulSoup(self.response,'lxml')
        _class = soup.find_all(attrs={'class':'viewy'})
        _list=[]
        for i in _class:
            z = i.find_all("a")[0].get_text()
            # print(z)
            j = i.find_all("td")[-1].get_text()
            if "Class" in j:
                dict = {'Flight number': z, 'Class': j.split()[1][1], 'New Fare': j.split()[3]}
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
            # print(j)
            self.flights[j[2].get_text()] = {}
            try:
                self.flights[j[2].get_text()]["Y"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[3].get_text(),"Unit Price":self.get_fares()["Y"],"Class":"Y"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["A"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[4].get_text(),"Unit Price":self.get_fares()["A"],"Class":"A"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["B"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[5].get_text(),"Unit Price":self.get_fares()["B"],"Class":"B"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["D"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[6].get_text(),"Unit Price":self.get_fares()["D"],"Class":"D"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["C"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[7].get_text(),"Unit Price":self.get_fares()["C"],"Class":"C"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["E"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[8].get_text(),"Unit Price":self.get_fares()["E"],"Class":"E"}
            except:
                pass
        self.flights_list=[]
        for i in self.flights:
            for j in self.flights[i]:
                time= f"{i[0:2]}:{i[2:]}"
                dict = {"Flight no.":self.flights[i][j]["Flight no."],"Class":self.flights[i][j]["Class"],"Time":time,"Maximum_Seats":self.flights[i][j]["Number of seats available"],"Unit_Price":self.flights[i][j]["Unit Price"]}
                self.flights_list.append(dict)
        improvise = self.get_special_fares()
        for i in improvise:
            for j in self.flights_list:
                if i["Flight number"] == j["Flight no."]:
                    if i["Class"]==j["Class"]:
                        j["Unit_Price"]=i["New Fare"]
        self.flights_list={"Buddha Air":self.flights_list}
        return self.flights_list


    def get_data(self,flight_number,class_name,nop):
        classes = {'Y':'1','A':'2','B':'3','D':'4','C':'5','E':'6'}
        class_name = classes[class_name]
        soup = BeautifulSoup(self.response,'lxml')
        flights = soup.find_all(attrs={'class':'viewy'})
        data={}
        flight_data={}
        for i in flights:
            flight_data[i.a.get_text()[:6]]={i.find(attrs={'name':f'unid{flights.index(i)+1}'})['name']:i.find(attrs={'name':f'unid{flights.index(i)+1}'})['value']}
            data[i.find(attrs={'name':f'fd{flights.index(i)+1}'})['name']]=i.find(attrs={'name':f'fd{flights.index(i)+1}'})['value']
            data[i.find(attrs={'name':f'unid{flights.index(i)+1}'})['name']]=i.find(attrs={'name':f'unid{flights.index(i)+1}'})['value']
            data[f'mclass{flights.index(i)+1}']='1'
            data[f'mpax{flights.index(i)+1}']=''
            data[f'open{flights.index(i)+1}']='F'
        flight_index= flight_data[flight_number]
        for i in flight_index:
            flight_index_ = ''
            for i in i:
                try:
                    i = int(i)
                    i = str(i)
                    flight_index_+=i
                except:
                    pass

        
        data[f'mclass{flight_index_}']=class_name
        data[f'mpax{flight_index_}']=nop
        data['proceed']= 'GO'
        data['valOft']= '9'
        data['cked']= ''
        data['munid']= flight_index[f'unid{flight_index_}']
        data['mclass']= class_name
        data['mopen']= ''
        data['mpax']= nop
        data['openbooking']= ''

        return data


    def get_referer(self,flight_number,class_name,nop):
        soup = BeautifulSoup(self.response,'html.parser')
        flights = soup.find_all(attrs={'class':'viewy'})
        cnt = len(flights)
        referer = 'http://r2.buddhaair.com/u4OnlineReservation/main.jsp?'
        data = self.get_data(flight_number,class_name,nop)
        # print(data)
        for i in flights:
            au = str(i.font).split('<font color="#FFFFCC" face="Verdana, Arial, Helvetica, sans-serif">')[1].split('</font>')[0]
            referer+=f"&au{flights.index(i)+1}={au}&unid{flights.index(i)+1}={data[f'unid{flights.index(i)+1}']}&tt1=T"
        sector = i.font.find_all('td')[0].get_text()
        referer+=f"&cnt={cnt}&flt_date={data['fd1']}&sp={sector}"
        return referer


    def book(self,flight_number,class_name,nop):
        headers = {
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

        headers['Referer']=self.get_referer(flight_number,class_name,nop)

        data = self.get_data(flight_number,class_name,nop)
        response = self.session.post('http://r2.buddhaair.com/u4OnlineReservation/reservation.jsp', headers=headers, data=data, verify=False)
        # print(response)
# session = re_login(Login())
# results = Search(session,'10','NOV','2021','BIR','KTM')
# # print(results)
# f = Fetch(results,session).book(flight_number='U4 718',class_name='E',nop='2')
# f = Fetch(results)
# # json = f.get_special_fares()
# # print(json)
# json = f.get_flight_and_seats()
# print(json)