import smtplib
from twilio.rest import Client

def getfile():
    file = open('rawdata.txt')
    return file



def _file(action):
    if action == 'open':
        _file = open('rawdata.txt')
        return _file
    elif action == 'close':
        try:
            _file.close()
        except:
            pass

class messages:

    
    def __init__(self,_file):
        self._file=_file
        raw_data = self._file('open')
        self.indexes = [index for index, value in enumerate(raw_data.readlines()) if value == 'eticket\n']
        self._file('close')

    
    def get_name(self):
        names = [] 
        for name in self.indexes:
            raw_name = self._file('open').readlines()[name+4]
            self._file('close')
            r = raw_name.split()
            r.pop(0)
            r.pop(0)
            r.pop(-2)
            r.pop(-1)

            item = r[-1]
            i = r.index(item)
            name =''
            for words in r:
                if len(r) == i:
                    name += words
                    f = name[0]
                    name.replace(name[0],f) 

                else:
                    name += words + ' '
                    f = name[0]
                    name.replace(name[0],f)
            name = 'Passenger Name : '+name
            names.append(name)
        return names


    def get_fund_type(self):
        fund_types = []
        for ftype in self.indexes:
            raw_fund_type = self._file('open').readlines()[ftype+5]
            self._file('close')
            fund_type = raw_fund_type.split()
            fund_type = fund_type[-1]
            fund_type = f'Ticket type : {fund_type.lower()}'
            fund_types.append(fund_type)
        return fund_types

    def get_dest(self):
        dests=[]
        for d in self.indexes:
            raw_from = self._file('open').readlines()[d+11]
            rf = raw_from.split()
            frm=rf[1]+' '+rf[2]
            self._file('close')
            self._file('open')
            raw_to = self._file('open').readlines()[d+12]
            rt=raw_to.split()
            to=rt[1]+' '+rt[2]
            dests.append(f'From : {frm} \nTo : {to}')
        return dests

    def get_creds(self):
        creds = []
        for c in self.indexes:
            raw_creds = self._file('open').readlines()[c+3]
            self._file('close')
            rc = raw_creds.split()
            pnr = rc[1]
            tkt= rc[4]
            creds.append(f'PNR : {pnr} & Ticket Number : {tkt}')
        return creds

    def get_time_and_date(self):
        times_and_dates=[]
        for times in self.indexes:
            raw_date_and_time = self._file('open').readlines()[times+13]
            dt = raw_date_and_time.split()
            date = dt[2]
            time = dt[4]
            times_and_dates.append(f'Flight Date : {date} \nFlight Time : {time}')
        return times_and_dates

    def get_fare(self):
        fares=[]
        for f in self.indexes:
            fare=self._file('open').readlines()[f+28]
            self._file('close')
            currency=self._file('open').readlines()[f+18]
            self._file('close')
            fares.append(f'Total Fare : {fare.strip()} {currency}')
        return fares






def give_message():
    m=messages(_file)
    
    length =len([index for index, value in enumerate(_file('open').readlines()) if value == 'eticket\n'])
    v = 0
    k = 4
    print(length)
    if length > 4:
        message = []
        if length % 5 == 0:
            for j in range(int(length+1/5)):
                msg='Dear Passenger,\nYour ticket itenary\n\n'
                for i in range(v,k):
                    me = f'{m.get_creds()[i]}\nAirlines : Buddha Air \n{m.get_name()[i]}\n{m.get_dest()[i]}\n{m.get_time_and_date()[i]}\n{m.get_fare()[i]}{m.get_fund_type()[i]}\n\n'
                    msg+=me
                    # msg = msg+'\n***Airport time is one hour eariler than flight time.***\nAgency Contact Number : 9851189900 , 014511047\nhave a safe and pleasant journey'
                v=k
                k=k+5
                message.append(msg)
        else:
            mod = length % 5 
            print(int((length+1)/5))
            for j in range(int((length+1)/5)):
                msg='Dear Passenger,\nYour ticket itenary\n\n'
                for i in range(v,k):
                    me = f'{m.get_creds()[i]}\nAirlines : Buddha Air \n{m.get_name()[i]}\n{m.get_dest()[i]}\n{m.get_time_and_date()[i]}\n{m.get_fare()[i]}{m.get_fund_type()[i]}\n\n'
                    msg+=me
                    # msg = msg+'\n***Airport time is one hour eariler than flight time.***\nAgency Contact Number : 9851189900 , 014511047\nhave a safe and pleasant journey'
                v=k+1
                if length-k >5:
                    k=k+5
                elif length-k ==5:
                    k=k+4
                else:
                    k = length-k
            message.append(msg)    
            for j in range(mod):
                msg='Dear Passenger,\nYour ticket itenary\n\n'
                for i in range(k,k+mod):
                    me = f'{m.get_creds()[i]}\nAirlines : Buddha Air \n{m.get_name()[i]}\n{m.get_dest()[i]}\n{m.get_time_and_date()[i]}\n{m.get_fare()[i]}{m.get_fund_type()[i]}\n\n'
                    msg+=me
                    # msg = msg+'\n***Airport time is one hour eariler than flight time.***\nAgency Contact Number : 9851189900 , 014511047\nhave a safe and pleasant journey'
            message.append(msg) 
    else:
        message = 'Dear Passenger,\nYour ticket itenary\n\n'
        for i in range(len([index for index, value in enumerate(_file('open').readlines()) if value == 'eticket\n'])):
            me = f'{m.get_creds()[i]}\nAirlines : Buddha Air \n{m.get_name()[i]}\n{m.get_dest()[i]}\n{m.get_time_and_date()[i]}\n{m.get_fare()[i]}{m.get_fund_type()[i]}\n\n'
            message+=me
        # message = message+'\n***Airport time is one hour eariler than flight time.***\nAgency Contact Number : 9851189900 , 014511047\nhave a safe and pleasant journey'
    return message

def sendEmail(to):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aht.alert@gmail.com', 'dtnhrlkdxspezffp')
    server.sendmail('aht.alert@gmail.com', to, give_message())
    server.close()

def twilio_send_msg(to,message):
    
    print(len(message))
    account_sid = 'ACe7e0a436b499ea01505a29707af5139b'
    auth_token = 'aecb3ae9dd2137e3e2160652a0e2d466'

    client = Client(account_sid,auth_token)
    if type(message) == list:
        for i in range(len(message)):
            client.messages.create(body=message[i]+'\n***Airport time is one hour eariler than flight time.***\nAgency Contact Number : 9851189900 , 014511047\nhave a safe and pleasant journey',
                        from_='+12062038170',
                        to='+977'+to
                    )    
    else:
        client.messages.create(body=message+'\n***Airport time is one hour eariler than flight time.***\nAgency Contact Number : 9851189900 , 014511047\nhave a safe and pleasant journey',
                            from_='+12062038170',
                            to='+977'+to
                        )    



        
