import main


import json

a = main.GunaAir()
a.get_logged_in_session()
dp = open('guna_air/tickets.json', 'r')
data = json.load(dp)['tickets']
# print(data)
total = len(data)
fp = open('guna_air/names.json', 'r')
det = json.load(fp)
count = 1
error_count = 0
f = open('guna_air/names.json', 'r')
d = json.load(f)
a_list=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
ticket_numbers = [i['ticket_number'] for i in det]
for i in data:
    if i['ticket_number'] not in ticket_numbers:
        try:
            print(f"{count} Out of {total} and {error_count} error(s) found so far")
            pnr,name,rd,i['flight_number'] = a.search_pnr_by_ticket_number(i['ticket_number'])
            print(name)
            i['name'] = name
            i['pnr'] = pnr

            date_list = rd.split()
            time = date_list[-1]
            date_list.remove(time)
            date_list[2] = '20'+date_list[2]
            
            date = date_list[2]+"-"+str(a_list.index(date_list[1])+1)+"-"+date_list[0]
            print(date)
            i['flight_date'] = date
            i['flight_time'] = time
            i['Airline'] = "Guna Air"
            d.append(i)

            
        except:
            error_count +=1
            errors = {}
            errors['data'] = i
            fep = open('guna_air/errors.json', 'r')
            delt = json.load(fep)
            delt.append(errors)
            flep = open('guna_air/errors.json', 'w+')
            json.dump(delt,flep)
    count +=1
    print(count)
fp = open('guna_air/names.json', 'w+')
json.dump(d,fp)
   
    

