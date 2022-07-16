import requests

cookies = {
    'JSESSIONID': 'C4E4AD96E49CAAD30CDDF12D7671FF5F.tomcat2',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://r2.buddhaair.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://r2.buddhaair.com/u4OnlineReservation/left.jsp',
    'Accept-Language': 'en-US,en;q=0.9',
}

params = (
    ('viewopt', 'view'),
)

data = {
  'ddd': '03',
  'mmm': 'OCT',
  'yyy': '2021',
  'fromsector': 'KTM',
  'tosector': 'BDP',
  'searchby': 'PNR',
  'searchval': ''
}

response = requests.post('http://r2.buddhaair.com/u4OnlineReservation/fdetail.jsp', headers=headers, params=params, cookies=cookies, data=data, verify=False)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('http://r2.buddhaair.com/u4OnlineReservation/fdetail.jsp?viewopt=view', headers=headers, cookies=cookies, data=data, verify=False)