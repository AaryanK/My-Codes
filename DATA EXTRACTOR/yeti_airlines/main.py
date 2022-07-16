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



from http import cookies
import bs4
import requests
# from .base import AirlineWebsite



class YetiAir(AirlineWebsite):
    def __init__(self):
        base_url = "http://res.yetiairlines.com/b2b/"
        super().__init__(base_url)
        self.cookies=self.get_cookies(self.session)

    def login(self):
        cookies = self.cookies
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': '*/*',
            'Origin': 'http://res.yetiairlines.com',
            'Referer': 'http://res.yetiairlines.com/b2b/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '{"userName":"antu","PassWord":"Aaryan330599","companyname":"antu"}'

        session = requests.Session()
        response = session.post('http://res.yetiairlines.com/b2b/WebService/BaseService.asmx/UserLogOn', headers=headers, cookies=cookies, data=data, verify=False)
        

        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://res.yetiairlines.com/b2b/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = session.get('http://res.yetiairlines.com/b2b/', headers=headers, cookies=cookies, verify=False)

        return session
    
    def get_logged_in_session(self,response=False):
        log_1 = self.login()
        
        self.session = log_1


    def search_for_flights(self,ddd,mmm,yyy,fromsector,tosector,passenger_count=1):
        session = self.session
        cookies = cookies = {
                    'ASP.NET_SessionId': 'xwktbbyturyeoc45g2duoz45',
                }
        yy= yyy
        mm=mmm
        MONTHS = {"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"}
        for i in MONTHS:
            if MONTHS[i] == mm:
                mm = i
        dd = ddd
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': '*/*',
            'Origin': 'http://res.yetiairlines.com',
            'Referer': 'http://res.yetiairlines.com/b2b/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '{"fromAirport":"KTM","toAirport":"BDP","dateFrom":"20211005","dateTo":"","iAdult":"1","iChild":"0","iInfant":"0","BDClass":"","isSearchGroup":"0","FareSelect":"","dayRange":"0","transit_flag":"false","direct_flag":"true","require_passenger_title_flag":"false","require_passenger_gender_flag":"false","require_date_of_birth_flag":"true","require_document_details_flag":"true","require_passenger_weight_flag":"false","OriginName":"Kathmandu","DestinationName":"Bhadrapur","show_redress_number_flag":"true","special_service_fee_flag":"true","currency":"NPR","bNoVat":false,"strPromoCode":"","strIPAddress":"","iOther":0,"otherPassengerTypeCode":""}'
        import json
        data = json.loads(data)
        data["toAirport"]=tosector
        data["fromAirport"]=fromsector
        data["dateFrom"]=f"{yy}{mm}{dd}"
        data["iAdult"]=passenger_count
        data = json.dumps(data)
        response = session.post('http://res.yetiairlines.com/b2b/WebService/BaseService.asmx/getFlightAvailabilityFormMultiCurrency', headers=headers, cookies=cookies, data=data, verify=False)
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': '*/*',
            'Origin': 'http://res.yetiairlines.com',
            'Referer': 'http://res.yetiairlines.com/b2b/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '{"move":"next"}'

        response = session.post('http://res.yetiairlines.com/b2b/WebService/UtilService.asmx/GetNextWorkFlowStep', headers=headers, cookies=cookies, data=data, verify=False)

        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://res.yetiairlines.com/b2b/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = session.get('http://res.yetiairlines.com/b2b/', headers=headers, cookies=cookies, verify=False)
        soup = bs4.BeautifulSoup(response.content,'html.parser')
        self.soup = soup
        self.js = {}
        self.flights={}
        return response.content
        

    def get_flight_and_seats(self,fare="NPR"):
        table = self.soup.find(id="tabOutward")
        trs = table.find_all(['tr','tbody'])
        trs = trs[:-1]
        trs=trs[1:]
        flight_name = ""
        new_list = []
        for i in trs:
            td = i.find_all("td")
            if "YT" in td[0].get_text():
                flight_name = td[0]
                new_list.append(td)
            else:
                td[0]=flight_name
                new_list.append(td)
        self.flights_list=[]
        for i in new_list:
            fare = i[8].get_text()
            fare = fare.split(",")
            fare = fare[0]+fare[1]
            fare = fare.split(".")
            if int(fare[1])>1:
                fare = int(fare[0])+1
            else:
                fare = fare[0]
            dict = {"Flight no.":f"{i[0].get_text()[0:2]} {i[0].get_text()[26:29]}","Class":i[6].get_text(),"Time":i[3].get_text(),"Maximum_Seats":i[7].get_text(),"Unit_Price":fare}
            self.flights_list.append(dict)
        self.flights_list={"Yeti Airlines":self.flights_list}
        return self.flights_list
    
    def individual_book(self,ddd,mmm,yyy,fromsector,tosector,nop,flight_number,classname,passengers):
        json_data = {
        'OutwardFlightFareId': '{2D4A8617-C6EA-4DF4-BAE8-EA6F39D47734}|{1DE15B09-2510-4DA8-BC58-D50C4ED5CC0E}|||2022-05-16T00:00:00|1330|1400',
        'ReturnFlightFareID': '',
        'OutWardDateFligh': '20220416_13_30',
        'OutSelectType': 'FIRM',
        'RetSelectType': 'FIRM',
        }

        headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json; charset=UTF-8',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'ASP.NET_SessionId=oed5j245cwf54r45azvuft45; _fbp=fb.1.1637678224640.1500946324; _ga=GA1.2.1762368887.1637678226; _gid=GA1.2.1825027642.1652599067',
                    'Origin': 'http://res.yetiairlines.com',
                    'Referer': 'http://res.yetiairlines.com/b2b/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47',
                }
        
        self.search_for_flights(ddd,mmm,yyy,fromsector,tosector,passenger_count=nop)
        table = self.soup.find(id="tabOutward")
        # print(table)
        trs = table.find_all(['tr','tbody'])
        trs = trs[:-1]
        trs=trs[1:]
        flight_name = ""
        new_list = []
        for i in trs:
            td = i.find_all("td")
            if "YT" in td[0].get_text():
                flight_name = td[0]
                new_list.append(td)
            else:
                td[0]=flight_name
                new_list.append(td)
        for i in new_list:
            if flight_number == f"{i[0].get_text()[0:2]} {i[0].get_text()[26:29]}" and classname == i[6].get_text():
                json_data['OutwardFlightFareId'] = i[-2].find("input")["value"]
                json_data['OutWardDateFligh'] = self.date+"_"+i[3].get_text()[:2]+"_"+i[3].get_text()[3:5]

                response = self.session.post('http://res.yetiairlines.com/b2b/WebService/BaseService.asmx/GetSelectFlight', cookies=self.cookies, headers=headers, json=json_data, verify=False)
                json_data = {
                    'move': 'next',
                }

                response = self.session.post('http://res.yetiairlines.com/b2b/WebService/UtilService.asmx/GetNextWorkFlowStep', cookies=self.cookies, headers=headers, json=json_data, verify=False)
                response = self.session.post('http://res.yetiairlines.com/b2b/WebService/UtilService.asmx/loadstep4', cookies=self.cookies, headers=headers, verify=False)                    
                response = self.session.get(self.BASE_URL,cookies=self.cookies)
                json_data = {
                        'passengerXml': '<Passengers><Passenger><passenger_id>d0f69614-c6d7-4da9-b147-96c61c1e5f17</passenger_id><client_number></client_number><client_profile_id>00000000-0000-0000-0000-000000000000</client_profile_id><passenger_profile_id>00000000-0000-0000-0000-000000000000</passenger_profile_id><passenger_type_rcd>ADULT</passenger_type_rcd><employee_number></employee_number><title_rcd>MR|M</title_rcd><lastname>A</lastname><firstname>B</firstname><middlename></middlename><nation>NP</nation><documenttype></documenttype><documentnumber></documentnumber><issueplace></issueplace><issuedate></issuedate><expireddate></expireddate><DOB></DOB><company_phone_business></company_phone_business><company_phone_mobile></company_phone_mobile><company_phone_home></company_phone_home><contact_name></contact_name><passport_birth_place></passport_birth_place><passenger_weight>0</passenger_weight><wheelchair_flag>0</wheelchair_flag><vip_flag>0</vip_flag><window_seat_flag>0</window_seat_flag><address_line1></address_line1><address_line2></address_line2><street></street><province></province><city></city><zip_code></zip_code><po_box></po_box><country_rcd></country_rcd></Passenger></Passengers>',
                        'Remark': '',
                        'Remark2': '',
                        'strContact': '<contact><ContactPerson>ANTUHILL TRAVEL  AND  TOURS</ContactPerson><HomePhone></HomePhone><Email>antutravel@gmail.com</Email><MobilePhone>01-4238057/ 01-4215126/01-4263957/9851189900</MobilePhone><BusinessPhone></BusinessPhone><Language>EN</Language><GroupName></GroupName><CostCenter></CostCenter><PurchaseOrder></PurchaseOrder><ProjectNumber></ProjectNumber></contact>',
                        'xmlMailList': '',
                    }
                json_data['passengerXml'] = self.get_passenger_xml(response,nop=nop,passengers=passengers)
                response = self.session.post('http://res.yetiairlines.com/b2b/WebService/UtilService.asmx/savestep4', cookies=self.cookies, headers=headers, json=json_data, verify=False)

                json_data = {
                    'move': 'next',
                }

                response = self.session.post('http://res.yetiairlines.com/b2b/WebService/UtilService.asmx/GetNextWorkFlowStep', cookies=self.cookies, headers=headers, json=json_data, verify=False)
                response = requests.post('http://res.yetiairlines.com/b2b/WebService/UtilService.asmx/loadssr', cookies=self.cookies, headers=headers, verify=False)
                response = self.session.get(self.BASE_URL,cookies=self.cookies)
                json_data = {
                    'ssrxml': '<Serices><Service><passenger_id>null</passenger_id><fee_id>00000000-0000-0000-0000-000000000000</fee_id><fee_rcd>null</fee_rcd><service_name>null</service_name><fee_amount_incl>null</fee_amount_incl><service_on_request_flag>null</service_on_request_flag><flight_id>null</flight_id></Service></Serices>',
                }

                response = self.session.post('http://res.yetiairlines.com/b2b/WebService/UtilService.asmx/savessrstep', cookies=self.cookies, headers=headers, json=json_data, verify=False)

                json_data = {
                    'move': 'next',
                }

                response = self.session.post('http://res.yetiairlines.com/b2b/WebService/UtilService.asmx/GetNextWorkFlowStep', cookies=self.cookies, headers=headers, json=json_data, verify=False)
                response = self.session.post('http://res.yetiairlines.com/b2b/WebService/UtilService.asmx/loadstep5', cookies=self.cookies, headers=headers, verify=False)
                response = self.session.get(self.BASE_URL,cookies=self.cookies)
                response = self.session.post('http://res.yetiairlines.com/b2b/WebService/UtilService.asmx/loadstep5PostPaid', cookies=self.cookies, headers=headers, verify=False)
                response = self.session.post('http://res.yetiairlines.com/b2b/WebService/Payment.asmx/Paylater', cookies=self.cookies, headers=headers, verify=False)
                response = self.session.get(self.BASE_URL,cookies=self.cookies)
                soup = BeautifulSoup(response.content.decode(),'lxml')
                json = {}
                json["STATUS"] = "Success"
                json["AIRLINE"] = "Yeti Air"
                json['PNR'] = soup.find(attrs={'class':'BookingRefItenerary'}).get_text().split("Booking Details:")[1].split()[0]
                json['FLIGHT_DATE_TIME']={}
                json['BOOKING_EXPIRY']={}
                json['FLIGHT_DATE_TIME']['DATE'],json['FLIGHT_DATE_TIME']['TIME'] =soup.find(attrs={'class':'TBLYourItinerary'}).find("td",attrs={'class':"BodyCOL4"}).get_text(),soup.find(attrs={'class':'TBLYourItinerary'}).find("td",attrs={'class':"BodyCOL5"}).get_text() 
                raw_date_time = soup.find(attrs={'class':'Itinerary-Pay'}).get_text().split("Please pay within                 ")[1]
                json['BOOKING_EXPIRY']['DATE'],json['BOOKING_EXPIRY']['TIME']= raw_date_time.split()[0],raw_date_time.split()[1]
                json["FLIGHT_NUMBER"] = flight_number 
                json['CLASS']=classname 
                json['UNIT_PRICE'] = soup.find(attrs={'class':'TBLTikets'}).find_all("td",attrs={'class':'BodyCOL6'})[0].get_text()
                return json
    
    def get_flight_time(self,ticketnumber):
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://res.yetiairlines.com/b2b/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = self.session.get('http://res.yetiairlines.com/b2b/', headers=headers, cookies=self.cookies, verify=False)
        json_data = {
            'isBack': 'false',
        }

        response = self.session.post('http://res.yetiairlines.com/b2b/WebService/ReportService.asmx/LoadBookingReport', cookies=self.cookies, headers=headers, json=json_data, verify=False)

        json_data = {
            'PagePerRows': '25',
            'selectpage': '0',
            'includepageing': True,
            'xslfile': '/XSL/Reports/BookingReport.xsl',
            'ReportFrom': '',
            'ReportTo': '',
            'FlightFrom': '',
            'FlightTo': '',
            'Origin': '',
            'Destination': '',
            'Agency': '',
            'Airline': '',
            'Flight': '',
            'passenger': '',
            'bookingRef': '',
            'ticketNumber': f'{ticketnumber}',
        }

        response = self.session.post('http://res.yetiairlines.com/b2b/WebService/ReportService.asmx/GetBookings', cookies=self.cookies, headers=headers, json=json_data, verify=False)
        # response = self.session.get('http://res.yetiairlines.com/b2b/', headers=headers, cookies=self.cookies, verify=False)
        
        soup = bs4.BeautifulSoup(response.json()['d'],'lxml')
        booking_id = soup.find(attrs={'class':'BodyCOL2'}).find('a')['href'].split()[0].split('javascript:LoadBookingDetail')[1].replace("(","").replace(")","").replace("'","").split(",")[0]

        json_data = {
            'bookingid': f'{booking_id}',
            'origin': '',
            'destination': '',
            'reportFrom': 'dd/mm/yyyy',
            'reportTo': 'dd/mm/yyyy',
            'reportName': 'BookingReport',
            'formOfPayment': '',
            'formOfPaymentSubtype': '',
            'Drill': '',
            'strflightdatefrom': 'dd/mm/yyyy',
            'strflightdateto': 'dd/mm/yyyy',
            'Airline': '',
            'FlightNumber': '',
            'strPassengerName': '',
            'strbookingReference': '',
            'strtickerNumber': f'{ticketnumber}',
            'page': 1,
        }

        response = self.session.post('http://res.yetiairlines.com/b2b/WebService/ReportService.asmx/LoadBookingDetail', cookies=self.cookies, headers=headers, json=json_data, verify=False)
        soup = bs4.BeautifulSoup(response.json()['d'],'lxml')
        return soup.find(attrs={'class':'TBLYourItinerary'}).find(attrs={'class':'BodyCOL1'}).get_text(),soup.find(attrs={'class':'TBLYourItinerary'}).find(attrs={'class':'BodyCOL5'}).get_text()