from django.shortcuts import render,redirect
import datetime
from django.contrib.sites.shortcuts import get_current_site
import requests
from api.Ticket_Sectors.Domestic.main import time_sort

# Create your views here.
variables = {}

def Home(request):
    return render(request,"index.html")

def Search_flights(request):
    variables = {}

    x = datetime.datetime.now()
    variables['minimum_date'],variables['default_date'] = str(x)[0:10],str(x)[0:10]
    variables["FROM"],variables["TO"]="KTM","BDP"
    variables["demanded"]=1

    if request.method =="POST":
        FROM = request.POST.get("FROM")
        TO = request.POST.get("TO")
        DATE = request.POST.get("DATE")
        Number = int(request.POST.get("Number"))
        

        return redirect("results",date=DATE,dest=f"{FROM}-{TO}",number=Number)

    return render(request,"staff/search_flights.html",variables)

def search_flights(request,date,dest,number):
    variables={}
    # final_dict=[]
    site = get_current_site(request)
    final_dict = requests.get(f"http://{site}/api/domestic_search?date={date}&dest={dest}")
    json = final_dict.json()
    final_dict = []
    if json["status"] == "success":
        json.pop('status')
        for i in json:
                for j in json[i]:
                    # print(j)
                    if j["Maximum_Seats"]!="00":
                        dict = {"Airline":i,"Flight_Number":j["Flight no."],"Class":j["Class"],"Time":j["Time"],"Maximum_Seats":int(j["Maximum_Seats"]),"Unit_Price":j["Unit_Price"]}
                        final_dict.append(dict)
        final_dict = time_sort(final_dict)
        
        variables["demanded"] = int(number)
        variables["api_response"] = final_dict
        variables['default_date'] = date
        variables["FROM"],variables["TO"]=dest[0:3],dest[4:]
    

    if request.method =="POST":
        print(request.POST)
        MONTHS = {"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"}
        site = get_current_site(request)
        nop = str(request.POST.get('Number'))
        airline = str(request.POST.get('Airline') )
        flight_number = request.POST.get('Flight_Number')
        class_name = str(request.POST.get('Class'))
        DATE = str(request.POST.get("DATE"))
        FROM = str(request.POST.get("FROM"))
        TO = str(request.POST.get("TO"))
        yy = str(DATE[0:4])
        mm = str(DATE[5:7])
        dd = str(DATE[8:10])
        mm = str(MONTHS[mm])
        # print(len(flight_number))
        if flight_number:
            # if airline:
            response = requests.post(f'http://{site}/api/book_flight/{DATE}/{FROM}-{TO}/{airline}/{flight_number}/{class_name}/{nop}')
            print(response.content)
                
            response = response.json()
            
            if response["status"] == "Success":
                print(response)
                pnr = response['PNR']
                
                return redirect("save names",pnr=pnr)
            
        
        return redirect("results",date=DATE,dest=f"{FROM}-{TO}",number=nop)

    return render(request,'staff/search_results.html',variables)
        

def save_names_and_data(request,pnr):
    response = requests.get(f'http://{get_current_site(request)}/api/bookings/{pnr}')
    if response.content==b'No bookings':   
        return HttpResponse("Error get back dammit")
    else:
        response = response.json()
        print(response)
        response['nop'] = range(1,int(response['nop'])+1)
        variables['response'] = response
        ACCESSED = True
        return render(request,'save_names.html',variables)