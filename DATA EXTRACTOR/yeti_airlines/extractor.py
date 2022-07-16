import main 
import json

a  = main.YetiAir()
a.get_logged_in_session()

dp = open('yeti_airlines/tickets.json', 'r')
data = json.load(dp)['tickets']
dp.close()
# print(data)
total = len(data)
fp = open('yeti_airlines/names.json', 'r')
det = json.load(fp)
fp.close()
count = 1
error_count = 0
f = open('yeti_airlines/names.json', 'r')
# f.close()
d = json.load(f)
f.close()
ticket_numbers = [i['ticket_number'] for i in det]
for i in data:
    if i['ticket_number'] not in ticket_numbers:
        try:
            print(f"{count} Out of {total} and {error_count} error(s) found so far")
            i['flight_number'],i['flight_time'] = a.get_flight_time(i['ticket_number'])

            i['Airline'] = "Yeti Air"
            d.append(i)
            fp = open('yeti_airlines/names.json', 'w+')
            json.dump(d,fp)
            fp.close()
            
        except:
            error_count +=1
            errors = {}
            errors['data'] = i
            fep = open('yeti_airlines/errors.json', 'r')
            delt = json.load(fep)
            delt.append(errors)
            flep = open('yeti_airlines/errors.json', 'w+')
            json.dump(delt,flep)
            flep.close()
    count +=1
    print(count)

