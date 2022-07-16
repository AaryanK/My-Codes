import json
import requests
f = open("book_tickets.json","r")
bookings = json.load(f)

count = 1
posted_count=1
for i in bookings:
    if len(i['passengers'])!=0:
        r = requests.get(f"http://127.0.0.1:8000/bookings/?pnr={i['pnr']}").json()

        if r['pnr']==None:
            r = requests.post('http://127.0.0.1:8000/bookings/',data=i)
            print(f"{914+count} Bookings posted / 10373")
            count+=1
        else:
            print(f"{posted_count} Bookings already posted / 10373")
            posted_count+=1

