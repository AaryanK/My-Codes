from . import buddha_air
from . import shree_air
from . import yeti_airlines
import concurrent.futures

def time_sort(list):
    # list = [{'Airline': 'Buddha Air', 'Time': '07:00  ', 'Maximum_Seats': '07', 'Unit_Price': '9530'}, {'Airline': 'Buddha Air', 'Time': '07:00  ', 'Maximum_Seats': '01', 'Unit_Price': '8330'}, {'Airline': 'Buddha Air', 'Time': '09:40  ', 'Maximum_Seats': '07', 'Unit_Price': '9530'}, {'Airline': 'Buddha Air', 'Time': '09:40  ', 'Maximum_Seats': '03', 'Unit_Price': '8330'}, {'Airline': 'Buddha Air', 'Time': '12:30  ', 'Maximum_Seats': '07', 'Unit_Price': '9530'}, {'Airline': 'Buddha Air', 'Time': '12:30  ', 'Maximum_Seats': '03', 'Unit_Price': '8330'}, {'Airline': 'Buddha Air', 'Time': '15:35  ', 'Maximum_Seats': '07', 'Unit_Price': '9530'}, {'Airline': 'Buddha Air', 'Time': '15:35  ', 'Maximum_Seats': '03', 'Unit_Price': '8330'}, {'Airline': 'Buddha Air', 'Time': '17:25  ', 'Maximum_Seats': '07', 'Unit_Price': '9530'}, {'Airline': 'Buddha Air', 'Time': '17:25  ', 'Maximum_Seats': '03', 'Unit_Price': '8330'}, {'Airline': 'Shree Air', 'Time': '11:00  ', 'Maximum_Seats': '08', 'Unit_Price': '9600'}, {'Airline': 'Shree Air', 'Time': '11:00  ', 'Maximum_Seats': '05', 'Unit_Price': '8400'}, {'Airline': 'Shree Air', 'Time': '17:00  ', 'Maximum_Seats': '08', 'Unit_Price': '9600'}, {'Airline': 'Shree Air', 'Time': '17:00  ', 'Maximum_Seats': '01', 'Unit_Price': '8400'}]
    for i in list:
        i["Time"]=i["Time"][0:2]+i["Time"][3:5]
    
    money_list=[]
    for i in list:
        money_list.append(i['Time'])

    time_list = sorted(set(money_list))
    final_list=[]
    for i in time_list:
        for j in list:
            if j["Time"] == i:
                final_list.append(j)

    for i in final_list:
        i["Time"]= i["Time"][0:2]+":"+i["Time"][2:]

    return final_list
    

def execute(func,args=None):
    with concurrent.futures.ThreadPoolExecutor as executor:
        f1=executor.submit(func,args)
        return f1.result()


def fetch_buddha_air(dd,mm,yy,fromsector,tosector):
    try:
        session = buddha_air.re_login(buddha_air.Login())
        results = buddha_air.Search(session,dd,mm,yy,fromsector,tosector)

        f = buddha_air.Fetch(results,session)
        json = f.get_flight_and_seats()
        # print(json)
        return json
    except:
        return {}

def fetch_shree_air(dd,mm,yy,fromsector,tosector):
    try:
        
        session = shree_air.relogin(shree_air.login())
        results = shree_air.Search(session,dd,mm,yy,fromsector,tosector)
        json = shree_air.Fetch(results,session).get_flight_and_seats()
    
        print(json)
        return json
    except:
        return {}


def fetch_yeti_airlines(dd,mm,yy,fromsector,tosector,passenger_count=1):
    try:
        MONTHS = {"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"}
        for i in MONTHS:
            if MONTHS[i] == mm:
                mm = i
        session = yeti_airlines.login()
        results = yeti_airlines.Search(session,dd,mm,yy,fromsector,tosector,passenger_count)
        json = yeti_airlines.Fetch(results).get_flight_and_seats()
        # print(json)
        return json
    except:
        return {}

def book_buddha_air(dd,mm,yy,fromsector,tosector,flight_number,class_name,passenger_count):
    
    try:
        session = buddha_air.re_login(buddha_air.Login())
        results = buddha_air.Search(session,dd,mm,yy,fromsector,tosector)
        f = buddha_air.Fetch(results,session).book(flight_number,class_name,nop=passenger_count)
        return "Success"
    except:
        return "We have an error here"

def book_shree_air(dd,mm,yy,fromsector,tosector,flight_number,class_name,passenger_count):
    
    try:
        session = shree_air.relogin(shree_air.login())
        results = shree_air.Search(session,dd,mm,yy,fromsector,tosector)
        # shree_air.Fetch(results,session).get_flight_and_seats())
        f = shree_air.Fetch(results,session).book(flight_number,class_name,nop=passenger_count)
        return "Success"
    except:
        return "We have an error here"

    

def Search(dd,mm,yy,fromsector,tosector):
    final_dict={}
    executor = concurrent.futures.ThreadPoolExecutor()
    buddha_air = executor.submit(fetch_buddha_air,dd,mm,yy,fromsector,tosector).result()
    # print(buddha_air)
    shree_air=executor.submit(fetch_shree_air,dd,mm,yy,fromsector,tosector).result()
    yeti_airlines=executor.submit(fetch_yeti_airlines,dd,mm,yy,fromsector,tosector).result()

    # print(shree_air)
    for i in buddha_air:
        final_dict[i] = buddha_air[i]
    for i in shree_air:
        final_dict[i] = shree_air[i]
    for i in yeti_airlines:
        final_dict[i] = yeti_airlines[i]
    return final_dict


