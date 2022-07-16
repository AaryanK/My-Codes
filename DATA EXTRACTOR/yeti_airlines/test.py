from attr import attr
from bs4 import BeautifulSoup

# from main import BuddhaAir
file = open('yetip2.html','r')

soup = BeautifulSoup(file,'lxml')


tables = soup.find_all("table",attrs={'class':'table table-bordered'})
sales_table = tables[0]

sales = sales_table.find_all("tr")[1:]



# sales = sal

# # def flip_name(name):
# #     text = name.split("/")
# #     return text

# # a = BuddhaAir()
# # s = a.get_html_logged_in_session()
# def date_standarize_issue(date):
#     a=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
#     dd = date[:2]
#     mm = str(a.index(date[3:6].upper())+1)
#     yy = date[7:9]
#     return yy+"-"+mm+"-"+dd


# #Data sent from 7000:
print(len(sales))
tickets = []
for i in sales[1:-1]:
    td = i.find_all("td")
    # for count,i in enumerate(td):
    #     print(count,i)
#     # data = a.search_name_from_ticket(a.search_pnr_by_ticket_number(td[1].get_text()),td[1].get_text())
#     # print(data)
    if str(td[4].get_text().strip()) =="ADULT":
        p_type="Adult"
    elif str(td[4].get_text().strip()) =="CHILD":
        p_type="Child"
    if str(td[9].get_text())=="NPR":
        nationality = "Nepali"
    else:
        nationality="Foreign"
    
    js = {
        'ticket_number':td[1].get_text(),
        'pnr':td[2].get_text(),
        'name':td[3].get_text(),
        'p_type':p_type,
        'nationality':nationality,
        'issuedate':td[5].get_text().strip(),
        'flightdate':td[6].get_text().strip(),
        'sector':td[7].get_text(),
        'className':td[8].get_text(),
        'commission':str(float(td[13].get_text())),
        'fare':str(float(td[13].get_text())+float(td[14].get_text()))

    }
    print(js)
    tickets.append(js)
t = {}
t['tickets'] = tickets
print(t)
import json
f = open("tickets2.json","w")
json.dump(obj=t,fp=f)