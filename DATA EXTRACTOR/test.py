from bs4 import BeautifulSoup

# from main import BuddhaAir
file = open('data3.html','r')

soup = BeautifulSoup(file,'lxml')


tables = soup.find_all("table")
sales_table = tables[0]
sales = sales_table.find_all("tr", {"class": "style28"})


# def flip_name(name):
#     text = name.split("/")
#     return text

# a = BuddhaAir()
# s = a.get_html_logged_in_session()
def date_standarize_issue(date):
    a=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    dd = date[:2]
    mm = str(a.index(date[3:6].upper())+1)
    yy = date[7:9]
    return yy+"-"+mm+"-"+dd


#Data sent from 7000:
# print(len(sales))
tickets = []
for i in sales[1:-1]:
    td = i.find_all("td")
    # data = a.search_name_from_ticket(a.search_pnr_by_ticket_number(td[1].get_text()),td[1].get_text())
    # print(data)
    if str(td[3].get_text().strip()) =="ADL":
        p_type="Adult"
    elif str(td[3].get_text().strip()) =="CHD":
        p_type="Child"
    if str(td[4].get_text().strip())=="NEP":
        nationality = "Nepali"
    else:
        nationality="Foreign"
    
    js = {
        'ticket_number':td[1].get_text(),
        'name':td[2].get_text(),
        'p_type':p_type,
        'nationality':nationality,
        'issuedate':date_standarize_issue(td[5].get_text().strip()),
        'sector':td[6].get_text(),
        'className':td[7].get_text(),
        '$commission':str(float(td[11].get_text())),
        '$fare':str(float(td[12].get_text())+float(td[11].get_text())),
        'commission':str(float(td[16].get_text())),
        'fare':str(float(td[16].get_text())+float(td[17].get_text()))

    }
    print(js)
    tickets.append(js)
t = {}
t['tickets'] = tickets
import json
f = open("buddhaair/tickets.json","w")
json.dump(obj=t,fp=f)
    
    
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
#             sector = data['FROM'].split()[0]+"-"+data['TO'].split()[0]
#             date,time = data['D/T'].split('/')[0],data['D/T'].split('/')[1]
#             total_fare = float(td[16].get_text())+float(td[17].get_text())
            
#             print(f"SN:{td[0].get_text()} NAME:{name} TICKET:{td[1].get_text()} PNR NO:{a.search_pnr_by_ticket_number(td[1].get_text())} TYPE:{td[3].get_text()} NATIONALITY:{td[4].get_text()} ISSUEDATE:{td[5].get_text()} SECTOR:{td[6].get_text()} CLASS:{td[7].get_text()} {td[8].get_text()}{td[9].get_text()}{td[10].get_text()}{td[11].get_text()} {td[12].get_text()} {td[13].get_text()} {td[14].get_text()} {td[15].get_text()} COMMISSION:{td[16].get_text()} PAYMENT:{td[17].get_text()} TotalFare:{float(td[16].get_text())+float(td[17].get_text())} \n")
        
#         # print(f"SN:{td[0].get_text()} TICKET:{td[1].get_text()} PNR NO:{a.search_pnr_by_ticket_number(td[1].get_text())} TYPE:{td[3].get_text()} NATIONALITY:{td[4].get_text()} ISSUEDATE:{td[5].get_text()} SECTOR:{td[6].get_text()} CLASS:{td[7].get_text()} {td[8].get_text()}{td[9].get_text()}{td[10].get_text()}{td[11].get_text()} {td[12].get_text()} FARE(NPR){td[13].get_text()}{td[14].get_text()}{td[15].get_text()}{td[16].get_text()}{td[17].get_text()}")
#     except Exception as e:
#         print(e)
#         pass