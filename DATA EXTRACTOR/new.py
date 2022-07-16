import json
import requests

from sqlalchemy import except_
# from logging import exception

# from main import BuddhaAir




# a = BuddhaAir()
# a.get_logged_in_session()

f = open("ticnewkets.json","r")
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

# # new = {}
# # new['unidentified'],new['identified']=[],[]
# # u_count =1
# # i_count=1
# # for i in tickets:
# #     for j in tickets[i]:
# #         try:
# #             data = a.search_name_from_ticket(j['pnr'],j['ticket_number'])
# #             if data=={}:
# #                 new['unidentified'].append(j)
# #                 print(f"{u_count} Tickets did not find full names")
# #                 u_count+=1
# #             else:
# #                 j['passenger_name'] =data['passenger_name']
# #                 j['flight_number']=data['flight_number']
# #                 j['FROM']=data['FROM']
# #                 j['TO']=data['TO']
# #                 j['D/T']=data['D/T']
# #                 new['identified'].append(j)
# #                 print(f"{i_count} Tickets found full names")
# #                 i_count+=1
# #         except Exception as e:
# #             print(e)


# # f = open("ticnewkets.json","w")
# # json.dump(obj=new,fp=f)
# # # a.search_pnr_by_ticket_number()

def give_raw_name(i):
    if i[0]=="MSTR" or i[0]=="MASTER":
        i.pop(0)
        try:
            i[-1]=i[-1][:i[-1].index("(")]
            if i[-1]=="":
                i.pop(-1)
            pass
        except:
            pass
        name = ""
        for j in i:
            if i.index(j) !=-1:
                name+=j+" "
            else:
                name+=j
        return name
    elif i[0] =="MS" or i[0] =="MR" or i[0] =="MRS" or i[0] =="MRS." or i[0]=='MR.' or i[0]=="MASTER" or i[0]=="MISS" or i[0]=="MISS." or i[0]=="MIS":
        i.pop(0)
        name = ""
        for j in i:
            if i.index(j) !=-1:
                name+=j+" "
            else:
                name+=j
        return name
        

    else:
        name = ""
        for j in i:
            if i.index(j) !=-1:
                name+=j+" "
            else:
                name+=j
        return name

def give_name(name):
    if "MR" in name and "/" not in name:
        rn = name.split()
        n = give_raw_name(rn)
        return n


    elif "MR" not in name and "/" not in name:
        rn = name.split()
        n = give_raw_name(rn)
        return n
    
    else:
        return None

pnr_list = []
for i in tickets['identified']:
    if i['pnr'] not in pnr_list:
        pnr_list.append(i['pnr'])

pl = []
for i in tickets['identified']:

    # if "AARYA" in i['passenger_name']:
    #     print(i['passenger_name'])

    if "MR" in i['passenger_name'] and "/" not in i['passenger_name']:
        pl.append(i)

    elif "MR" not in i['passenger_name'] and "/" not in i['passenger_name']:
        pl.append(i)
d = []

for data in pl:
    r = requests.get('http://127.0.0.1:8000/bookings/?pnr='+data['pnr']).json()
    if r['pnr']!=None:
        json = {}
        # json['from_sector'],json['to_sector'] = data['FROM'],data['TO']
        # json['passenger_name'] = give_name(data['passenger_name']).strip()
        json['pnr'] = data['pnr']
        json['airlines'] ='Buddha Air'
        json['ticket_number'] = data['ticket_number']
        # json['flight_date'],json['flight_time']=date_standarize_flight(data['D/T'].split("/")[0]),data['D/T'].split("/")[1]
        json['commission'] = {'amount':float(data['commission']),'currency':'NPR'}
        if json['commission']['amount']==0:
            json['commission']={'amount':float(data['$commission']),'currency':'USD'}
        # json['ticket_class'] = data['className']
        # json['issued_at'] = data['issuedate']

        print(json)
        d.append(json)

            




#     # if "AARYA" in i['passenger_name']:
#     #     print(i['passenger_name'])

#     if "MR" in i['passenger_name'] and "/" not in i['passenger_name']:
#         rn = i['passenger_name'].split()
#         passenger_lists.append(rn)

#     elif "MR" not in i['passenger_name'] and "/" not in i['passenger_name']:
#         rn = i['passenger_name'].split()

#         passenger_lists.append(rn)

#     # elif "(" in i['passenger_name']:
#         # print(i['passenger_name'])
# # print(passenger_lists)
# # for i[0] in tickets["unidentified"]:
# #     if "(" in i['name']:
# #         print(i['name'])

# new_passenger_lists = []

# for i in passenger_lists:
#     if i[0]=="MSTR" or i[0]=="MASTER":
#         i.pop(0)
#         try:
#             i[-1]=i[-1][:i[-1].index("(")]
#             if i[-1]=="":
#                 i.pop(-1)
#             pass
#         except:
#             pass
#         name = ""
#         for j in i:
#             if i.index(j) !=-1:
#                 name+=j+" "
#             else:
#                 name+=j
#         new_passenger_lists.append(name)
#     elif i[0] =="MS" or i[0] =="MR" or i[0] =="MRS" or i[0] =="MRS." or i[0]=='MR.':
#         i.pop(0)
#         name = ""
#         for j in i:
#             if i.index(j) !=-1:
#                 name+=j+" "
#             else:
#                 name+=j
#         new_passenger_lists.append(name)

#     else:
#         name = ""
#         for j in i:
#             if i.index(j) !=-1:
#                 name+=j+" "
#             else:
#                 name+=j
#         new_passenger_lists.append(name)
    

# # print(new_passenger_lists)

# post_data = []
# pl = []
# for i in tickets['identified']:

#     # if "AARYA" in i['passenger_name']:
#     #     print(i['passenger_name'])

#     if "MR" in i['passenger_name'] and "/" not in i['passenger_name']:
#         pl.append(i)

#     elif "MR" not in i['passenger_name'] and "/" not in i['passenger_name']:
#         pl.append(i)

# # print(len(tickets['identified']),len(new_passenger_lists),len(passenger_lists),len(pl))
# # print(new_passenger_lists[-1],pl[-1])
# for i in range(len(pl)):
#     # print(give_name(pl[i]['passenger_name']))
#     if give_name(pl[i]['passenger_name']) == new_passenger_lists[i]:
#         js = {}
#         js['passenger_name'] = new_passenger_lists[i].strip()
#         js['p_type'] = pl[i]['p_type']
#         if pl[i]['$fare'] !="0.0":
#             js["nationality"]="Foreigner"
#         else:
#             js["nationality"]="Nepali"
#         if js in post_data:
#             pass
#         else:
#             print(js)
#             post_data.append(js)
import json    
f = open("comm_tickets.json","w")
json.dump(obj=d,fp=f)