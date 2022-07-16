from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession



class AirlineWebsite():
    def __init__(self,base_url):
        self.BASE_URL = base_url
        self.session = requests.Session()
        self.HTMLsession = HTMLSession()

    def get_cookies(self,session):
        cookies = session.get(self.BASE_URL).cookies.get_dict()
        return cookies

    def base_login(self,response=False):
        session= self.get_logged_in_session(response)
        return session

    def get_balance(self):
        self.balance = self.check_balance_individually()
        return self.balance

    def search_flights(self,ddd,mmm,yyy,fromsector,tosector,passenger_count=1):
        self.search_for_flights(ddd,mmm,yyy,fromsector,tosector)
        json = self.get_flight_and_seats()
        return json

    # def book(self,ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop):
        
        
    def book(self,ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop):
        return self.individual_book(ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop)




class BuddhaAir(AirlineWebsite):



    def __init__(self):
        base_url = "http://r2.buddhaair.com"
        super().__init__(base_url)
        self.cookies=self.get_cookies(self.session)

    def login(self,session):
        
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

        session.post('http://r2.buddhaair.com/Home/login.jsp', headers=headers,data=data, verify=False,cookies=self.cookies)
        return session

    def re_login(self,session,response=False):
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

        res = session.post('http://r2.buddhaair.com/u4OnlineReservation/rechkpwd.jsp', headers=headers_re, data=data_re, verify=False,cookies=self.cookies)
        
        return session


    def get_html_logged_in_session(self,response=False):
        log1 = self.login(self.HTMLsession)
        log2 = self.re_login(log1,response=response)

        return log2

    def get_logged_in_session(self,response=False):
        log_1 = self.login(self.session)
        log_2 = self.re_login(log_1,response=response)
        
        
        return log_2

    def search_for_flights(self,ddd,mmm,yyy,fromsector,tosector):
        session = self.get_logged_in_session()
        cookies = self.cookies
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

        data = {
        'ddd': ddd,
        'mmm': mmm,
        'yyy': yyy,
        'fromsector': fromsector,
        'tosector': tosector,
        'searchby': 'PNR',
        'searchval': ''
        }

        params = (
        ('viewopt', 'view'),
        )

        response = session.post('http://r2.buddhaair.com/u4OnlineReservation/fdetail.jsp', headers=headers, params=params, data=data, verify=False,cookies=cookies).content
        soup = bs4.BeautifulSoup(response,'html.parser')
        self.session = session
        self.response,self.soup = response,soup
        self.js,self.flights = {},{}
        return self.response,self.soup

    
    def get_fares(self,fare="NPR"):
        fares = self.soup.find(id="fare")
        trs = fares.find_all('tr')
        i = trs[4]
        a = i.find_all(['tr','td'])
        SECTOR = a[1].get_text()
        for i in trs[4:]:
            a = i.find_all(['tr','td'])
           
            a=a[1:]
            if len(a)>10:
                self.js['SECTOR'] = a[0].get_text()
                    
                self.js[a[1].get_text()]=a[6].get_text()
        return self.js

    def get_special_fares(self):
        soup = bs4.BeautifulSoup(self.response,'lxml')
        _class = soup.find_all(attrs={'class':'viewy'})
        _list=[]
        for i in _class:
            z = i.find_all("a")[0].get_text()
            # print(z)
            j = i.find_all("td")[-1].get_text()
            if "Class" in j:
                dict = {'Flight number': z[:6], 'Class': j.split()[1][1], 'New Fare': j.split()[3]}
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
            # print(j[2].get_text())
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
                        j["Orignal_Price"] = j["Unit_Price"]
                        j["Unit_Price"]=i["New Fare"]
        self.flights_list={"Buddha Air":self.flights_list}
        return self.flights_list

    def get_referer(self,flight_number,class_name,nop):
        soup = bs4.BeautifulSoup(self.response,'html.parser')
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
    
    def get_data(self,flight_number,class_name,nop):
        classes = {'Y':'1','A':'2','B':'3','D':'4','C':'5','E':'6'}
        class_name = classes[class_name]
        soup = bs4.BeautifulSoup(self.response,'lxml')
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
        data['valOft']= str(len(flights))
        data['cked']= ''
        data['munid']= flight_index[f'unid{flight_index_}']
        data['mclass']= class_name
        data['mopen']= ''
        data['mpax']= nop
        data['openbooking']= ''

        return data

    def search_pnr_by_name_by_ticket_number(self,ticket_number):
        data = {
        'ddd': '07',
        'mmm': 'APR',
        'yyy': '2022',
        'fromsector': 'BDP',
        'tosector': 'BDP',
        'searchby': 'Ticket Number',
        'searchval': ticket_number,
        }
        response = requests.post('http://r2.buddhaair.com/u4OnlineReservation/searchpage.jsp',cookies=self.cookies, data=data, verify=False)
        soup = BeautifulSoup(response.content,'lxml')
        return soup.find("table").find_all("tr")[3].find_all("td")[3].get_text()



    
    def search_pnr_by_ticket_number(self,ticketnumber):
        data = {
        'ddd': '07',
        'mmm': 'APR',
        'yyy': '2022',
        'fromsector': 'BDP',
        'tosector': 'BDP',
        'searchby': 'Ticket Number',
        'searchval': ticketnumber,
    }

        response = requests.post('http://r2.buddhaair.com/u4OnlineReservation/searchpage.jsp',cookies=self.cookies, data=data, verify=False)
        soup = BeautifulSoup(response.content,'lxml')
        return soup.find("table").find_all("tr")[3].find_all("td")[1].get_text()
    


    def search_flight_number_and_date_from_ticket_number(self,ticketnumber):
        data = {
        'ddd': '07',
        'mmm': 'APR',
        'yyy': '2022',
        'fromsector': 'BDP',
        'tosector': 'BDP',
        'searchby': 'Ticket Number',
        'searchval': ticketnumber,
    }

        response = requests.post('http://r2.buddhaair.com/u4OnlineReservation/searchpage.jsp',cookies=self.cookies, data=data, verify=False)
        soup = BeautifulSoup(response.content,'lxml')
        # print(soup.find("table").find_all("tr")[3].find_all("td")[4].get_text().upper())
        return soup.find("table").find_all("tr")[3].find_all("td")[4].get_text().upper(),"U4 "+soup.find("table").find_all("tr")[3].find_all("td")[5].get_text()[:3]





    def search_name_from_ticket(self,pnr,ticket_number):
        response = requests.get(f'http://r2.buddhaair.com/u4OnlineReservation/eticket.jsp?pnrno={pnr}',cookies=self.cookies,verify=False)
        soup = BeautifulSoup(response.content,'lxml')
        tables = soup.find_all(attrs={'class':'lebleblk'})
        data = {}
        for i in tables:
            spltted = i.get_text().split()
            if "PNR" in spltted and i.find_all("tr")[0].find_all("td")[3].get_text() == str(ticket_number):
                passenger_name = i.find_all("tr")[1].find_all("td")[1].get_text()
                data['passenger_name']= passenger_name
            if "Flt" in spltted:
                td= i.find_all("td")
                for j in td:
                    if j.get_text().lower().split() == ['flt','no']:
                        j_ind = td.index(j)
                        data['flight_number']=td[j_ind+1].get_text()
                        data['FROM']=td[j_ind+3].get_text()
                        data['TO']=td[j_ind+5].get_text()
                        data['D/T']=td[j_ind+7].get_text()
                

        return data


    def individual_book(self,ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop):
        self.search_for_flights(ddd,mmm,yyy,fromsector,tosector)
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
        headers['Referer']=self.get_referer(flight_number,classname,nop)
        data = self.get_data(flight_number,classname,nop)
        response = self.session.post('http://r2.buddhaair.com/u4OnlineReservation/reservation.jsp', headers=headers, data=data,cookies=self.cookies,verify=False)
        if "WE HAVE AN ERROR HERE" in response.content.decode():
            return {"status":"Error"}
        else:
            soup = bs4.BeautifulSoup(response.content.decode(),'lxml')

            json = {}
            json["status"] = "Success"
            json["Airline"] = "Buddha Air"
            json['PNR'] = soup.find(attrs={'class':'style1'}).get_text()
            json['BOOKING_EXPIRY']={}
            f = self.get_flight_and_seats()
            for i in f:
                for j in f[i]:
                    if j["Flight no."] == flight_number and j['Class']==classname:
                        json['TIME'] = j['Time']
                        json['flight_number'] = j["Flight no."]
                        json['Unit_Price'] = j['Unit_Price']
                        json['Class'] = j['Class']
                        # print(j['Time'])
                        break
            expiry = soup.find_all(attrs={'class':'style2'})
            # print(expiry)
            json['BOOKING_EXPIRY']['DATE'] = expiry[0].get_text()
            # print(json)
            time= f"{expiry[1].get_text()[0:2]}:{expiry[1].get_text()[2:]}"
            # print(time)
            json['BOOKING_EXPIRY']['TIME'] = time
            # print(json)
            # count+=1
            headers = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'en-US,en;q=0.9',
            }
            headers['Referer']=self.get_referer(flight_number,classname,nop)
            response = self.session.get('http://r2.buddhaair.com/u4OnlineReservation/main.jsp', headers=headers, cookies=self.cookies, verify=False)
            return json


        
# a = BuddhaAir()
# s = a.get_logged_in_session()

# # print(cookies)


# tables = soup.find_all("table")
# sales_table = tables[0]
# sales = sales_table.find_all("tr", {"class": "style28"})
# file = open("soup.pkl",'wb')
# pickle.dump(sales,file)

# def flip_name(name):
#     text = name.split("/")
#     return text


# f = open('test.txt','a')
# #Data sent from 7000:
# for i in sales:
#     td = i.find_all("td")
#     try:
#         data = a.search_name_from_ticket(a.search_pnr_by_ticket_number(td[1].get_text()),td[1].get_text())
#         name = data['passenger_name']
#         print(data)
#         if "/" not in name:
#             if "MR" in name or "MRS" in name or "MS" in name:
#                 try:
#                     name = name.split("MR")[1]
#                 except:
#                     try:
#                         name = name.split("MRS")[1]
#                     except:
#                         name = name.split("MS")[1]
            
#             if str(td[3].get_text().strip()) =="ADL":
#                 p_type="Adult"
#             elif str(td[3].get_text().strip()) =="CHD":
#                 p_type="Child"
#             if str(td[4].get_text().strip())=="NEP":
#                 nationality = "Nepali"
#             else:
#                 nationality="Foreign"
            
#             pnr = a.search_pnr_by_ticket_number(td[1].get_text())
#             r = requests.get(f"http://127.0.0.1:8000/bookings/?pnr={pnr}")
#             sector = data['FROM'].split()[0]+"-"+data['TO'].split()[0]
#             date,time = data['D/T'].split('/')[0],data['D/T'].split('/')[1]
#             total_fare = float(td[16].get_text())+float(td[17].get_text())
            
#             print(f"SN:{td[0].get_text()} NAME:{name} TICKET:{td[1].get_text()} PNR NO:{a.search_pnr_by_ticket_number(td[1].get_text())} TYPE:{td[3].get_text()} NATIONALITY:{td[4].get_text()} ISSUEDATE:{td[5].get_text()} SECTOR:{td[6].get_text()} CLASS:{td[7].get_text()} {td[8].get_text()}{td[9].get_text()}{td[10].get_text()}{td[11].get_text()} {td[12].get_text()} {td[13].get_text()} {td[14].get_text()} {td[15].get_text()} COMMISSION:{td[16].get_text()} PAYMENT:{td[17].get_text()} TotalFare:{float(td[16].get_text())+float(td[17].get_text())} \n")
        
#         # print(f"SN:{td[0].get_text()} TICKET:{td[1].get_text()} PNR NO:{a.search_pnr_by_ticket_number(td[1].get_text())} TYPE:{td[3].get_text()} NATIONALITY:{td[4].get_text()} ISSUEDATE:{td[5].get_text()} SECTOR:{td[6].get_text()} CLASS:{td[7].get_text()} {td[8].get_text()}{td[9].get_text()}{td[10].get_text()}{td[11].get_text()} {td[12].get_text()} FARE(NPR){td[13].get_text()}{td[14].get_text()}{td[15].get_text()}{td[16].get_text()}{td[17].get_text()}")
#     except Exception as e:
#         print(e)
#         pass

