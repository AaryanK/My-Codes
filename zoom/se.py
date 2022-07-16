#!/usr/bin/env python

from selenium import webdriver


links = {'maths':'https://us04web.zoom.us/wc/join/9562206942?wpk=wcpk45d618b025feeb5d287e59eaeffc2cbe',
         'nepali':'https://us04web.zoom.us/wc/join/2478253136?wpk=wcpk5fae43e84d911349e8a6548c7c271137',
         'science':'https://us04web.zoom.us/wc/join/8840743766?wpk=wcpk25255fda25c709e4e713092131000775',
         'eph':'https://us04web.zoom.us/wc/join/4639696441?wpk=wcpk56405c4e9414ba882517e244b9f6fee2',
         'social':'https://us04web.zoom.us/wc/join/8532062482?wpk=wcpk1a6512969006e4ce5a86503e10aa62c9',
         'computer':'https://us04web.zoom.us/wc/join/4563530400',
         'omaths':'https://us04web.zoom.us/wc/join/4413257070?wpk=wcpkf4e48ca54269451100f06f7eba16f7df'}


routine = {'sunday':{'09:00':'nepali',
                    '09:50':'science',
                    '11:00':'maths',
                    '11:50':'computer'},

            'monday':{'09:00':'nepali',
                    '09:50':'science',
                    '11:00':'maths',
                    '16:00':'computer'},

            'tuesday':{'09:00':'nepali',
                    '09:50':'science',
                    '11:00':'maths',
                    '11:50':'computer'},#ya 11:50 ko thau ma 15:05 haal

            'wednesday':{'09:00':'eph',
                    '09:50':'omaths',
                    '11:00':'social'},
            
            'thursday':{'09:00':'eph',
                    '09:50':'omaths',
                    '11:00':'social'},
                    
            'friday':{'09:00':'eph',
                    '09:50':'omaths',
                    '11:00':'social'}        
                    
            }


# today=datetime.datetime.now().strftime('%A').lower()




browser = webdriver.Chrome()
browser.get('chrome://dino')