from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from numpy import number
import requests
from .apis import main_api
import requests
import datetime



# Create your views here.
def home(request):
    return HttpResponse("Welcome to home")


def api(request,date,dest):
    MONTHS = {"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"}
    yy = date[0:4]
    mm = date[5:7]
    dd = date[8:10]
    frm = dest[0:3]
    to = dest[4:]
    # results = main_api.Search(session,ddd='04',mmm='10',yyy='2021',fromsector=frm,tosector=to)
    json = main_api.Search(dd,MONTHS[mm],yy,frm,to)
    return JsonResponse(json)

def search(request,date,dest,number):
    variables={}
    final_dict=[]
    response = requests.get(f"http://127.0.0.1:8000/api/{date}/{dest}")
    raw_dict = response.json()
    for i in raw_dict:
        for j in raw_dict[i]:
            # print(j)
            if j["Maximum_Seats"]!="00":
                dict = {"Airline":i,"Flight_Number":j["Flight no."],"Class":j["Class"],"Time":j["Time"],"Maximum_Seats":int(j["Maximum_Seats"]),"Unit_Price":j["Unit_Price"]}
                final_dict.append(dict)
    final_dict = main_api.time_sort(final_dict)
    variables["demanded"] = int(number)
    variables["api_response"] = final_dict
    variables['default_date'] = date
    variables["FROM"],variables["TO"]=dest[0:3],dest[4:]
    

    if request.method =="POST":
        print(request.POST)
        MONTHS = {"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"}

        nop = str(request.POST.get('Number'))
        airline = str(request.POST.get('Airline') )
        flight_number = str(request.POST.get('Flight_Number'))
        class_name = str(request.POST.get('Class'))
        DATE = str(request.POST.get("DATE"))
        FROM = str(request.POST.get("FROM"))
        TO = str(request.POST.get("TO"))
        yy = str(DATE[0:4])
        mm = str(DATE[5:7])
        dd = str(DATE[8:10])
        mm = str(MONTHS[mm])
        if flight_number:
            if airline == "Buddha Air":
                print(main_api.book_buddha_air(dd,mm,yy,FROM,TO,flight_number,class_name,nop))
            elif airline == "Shree Air":
                print(main_api.book_shree_air(dd,mm,yy,FROM,TO,flight_number,class_name,nop))

        
        return redirect("results",date=DATE,dest=f"{FROM}-{TO}",number=nop)

    return render(request,'search_results.html',variables)

def search_flights(request):
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
    # print(variables)
    return render(request,"search.html",variables)

def login(request):
    return render(request,"login.html")


def customer_search(request,name):
    return HttpResponse(f"Customer name is {name}")

def manage_customer(request):
    if request.method =="POST":
        name = request.POST.get("Customer_name")
        return redirect("customer_search",name=name)
    return render(request,"manage_customer.html")