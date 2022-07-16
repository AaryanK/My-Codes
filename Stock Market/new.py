import requests
import bs4


resp =requests.get('https://nepsealpha.com/nepse-data').text
soup = bs4.BeautifulSoup(resp, 'html.parser')



