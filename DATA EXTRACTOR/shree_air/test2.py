import bs4
file = open('Shree Airlines.html','r')
soup = bs4.BeautifulSoup(file,'lxml')


# soup = bs4.BeautifulSoup(file,'lxml')


tables = soup.find_all("table")
sales_table = tables[0]

sales = sales_table.find_all("tr")[6:]
sal = []
for count,i in enumerate(sales):
    if count % 2 != 0:
        sal.append(i)


sales = sal

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
print(len(sales))
tickets = []
for i in sales[1:-1]:
    td = i.find_all("td")
    # for count,i in enumerate(td):
    #     print(count,i)
    # data = a.search_name_from_ticket(a.search_pnr_by_ticket_number(td[1].get_text()),td[1].get_text())
    # print(data)
    if str(td[3].get_text().strip()) =="ADULT":
        p_type="Adult"
    elif str(td[3].get_text().strip()) =="CHILD":
        p_type="Child"
    if float(td[12].get_text())==0.0:
        nationality = "Nepali"
    else:
        nationality="Foreign"
    
    js = {
        'ticket_number':td[1].get_text(),
        'name':td[2].get_text(),
        'p_type':p_type,
        'nationality':nationality,
        'issuedate':date_standarize_issue(td[4].get_text().strip()),
        'sector':td[5].get_text(),
        'className':td[6].get_text(),
        '$commission':str(float(td[15].get_text())),
        '$fare':str(float(td[15].get_text())+float(td[16].get_text())),
        'commission':str(float(td[10].get_text())),
        'fare':str(float(td[10].get_text())+float(td[11].get_text()))

    }
    # print(js)
    tickets.append(js)
t = {}
t['tickets'] = tickets
print(t)