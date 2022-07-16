import json
import main

dp = open('data_corrector/base_data.json', 'r')
data = json.load(dp)['tickets']
# print(data)
total = len(data)
fp = open('data_corrector/names.json', 'r')
det = json.load(fp)
ticket_numbers = [i['ticket_number'] for i in det]
a = main.BuddhaAir()
a.get_logged_in_session()
count = 1
error_count = 0
f = open('data_corrector/names.json', 'r')
d = json.load(f)
a_list=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
for i in data:

    if i['ticket_number'] not in ticket_numbers:
        try:
            print(f"{count} Out of {total} and {error_count} error(s) found so far")
            name = a.search_pnr_by_name_by_ticket_number(i['ticket_number'])
            print(name)
            i['name'] = name
            date_and_time,i['flight_number'] = a.search_flight_number_and_date_from_ticket_number(i['ticket_number'])
            date_list = date_and_time.split()
            time = date_list[-1]
            date_list.remove(time)
            date_list[2] = '20'+date_list[2]
            
            date = date_list[2]+"-"+str(a_list.index(date_list[1])+1)+"-"+date_list[0]
            print(date)
            i['flight_date'] = date
            i['flight_time'] = time
            i['Airline'] = "Buddha Air"
            d.append(i)
            
        except:
            error_count +=1
            errors = {}
            errors['data'] = i
            fep = open('data_corrector/errors.json', 'r')
            delt = json.load(fep)
            delt.append(errors)
            flep = open('data_corrector/errors.json', 'w+')
            json.dump(delt,flep)
    count +=1
    print(count)
fp = open('data_corrector/names.json', 'w+')
json.dump(d,fp)


    # fp = open('data_corrector/names.json', 'r')
    # d = json.load(fp)
    # print("s for skip")
    # print("Is the name correct? (y/n)")
    # ans = input().lower()
    # dict_base = {
    #     "passenger_name": "SAGAR BASNET",
    #     "nationality": "Nepali"
    #     }
    # if ans == "":
    #     dict_base['passenger_name'] = name
    #     dict_base['nationality'] = i['nationality']
    #     d.append(dict_base)
    #     print("Added")
    #     count+=1
    #     fp = open('data_corrector/names.json', 'w+')
    #     json.dump(d,fp)
    # if ans =="n":
    #     print("Enter the preffered name")
    #     n = input().upper()
    #     name = n
    #     dict_base['passenger_name'] = name
    #     dict_base['nationality'] = i['nationality']
    #     d.append(dict_base)
    #     print("Added")
    #     count+=1
    #     fp = open('data_corrector/names.json', 'w+')
    #     json.dump(d,fp)
    
    # if ans == "s":
    #     print("Skipped")
    #     count+=1
    #     pass



