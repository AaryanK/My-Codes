''''Date : 1/16/2022 Amadeus api testing'''


import requests


client_id = 'LOlEiwfwSg3wKEIALfZL6yrA8Fo3gKHO'
client_secret = 'htPn79dHsSN6t7pJ'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
  'grant_type': 'client_credentials',
  'client_id': f'{client_id}',
  'client_secret': f'{client_secret}'
}

response = requests.post('https://test.api.amadeus.com/v1/security/oauth2/token', headers=headers, data=data)
token = response.json()['access_token']

headers = {
    'Authorization': f'Bearer {token}',
}

params = (
    ('originLocationCode', 'KTM'),
    ('destinationLocationCode','DEL'),
    ('departureDate','2022-01-17'),
    ('currencyCode','NPR'),
    ('adults',1)



)

response = requests.get('https://test.api.amadeus.com/v2/shopping/flight-offers', headers=headers, params=params)
response = response.json()['data']

for i in response:
    print(i)