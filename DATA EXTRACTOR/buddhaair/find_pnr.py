from main import BuddhaAir
import json
import requests



a = BuddhaAir()
a.get_logged_in_session()

f = open("tickets.json","r")
tickets = json.load(f)

def date_standarize_flight(date):
    try:
        a=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
        dd = date[:2]
        mm = str(a.index(date[3:6].upper())+1)
        yy = date[7:11]
        return yy+"-"+mm+"-"+dd
    except Exception as e:
        print(e)
        print(date)

new = {}
new['unidentified'],new['identified']=[],[]
u_count =1
i_count=1
for i in tickets:
    for j in tickets[i]:
        try:
            pnr = a.search_pnr_by_ticket_number(j['ticket_number'])
            data= a.search_name_from_ticket(pnr,j['ticket_number'])
            if data=={}:
                j['pnr'] = pnr
                new['unidentified'].append(j)
                print(f"{u_count} Tickets did not find full names")
                u_count+=1
            else:
                j['pnr']=pnr
                j['passenger_name'] =data['passenger_name']
                j['flight_number']=data['flight_number']
                j['FROM']=data['FROM']
                j['TO']=data['TO']
                j['D/T']=data['D/T']
                new['identified'].append(j)
                print(f"{i_count} Tickets found full names")
                i_count+=1
        except Exception as e:
            print(e)


f = open("ticnewkets.json","w")
json.dump(obj=new,fp=f)