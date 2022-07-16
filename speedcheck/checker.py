import speedtest
import threading
import  os
tester = speedtest.Speedtest()

class Test:
    
    def __init__(self,checker):
        self.tester = checker

    def download(self):
        tester = self.tester
        download = f'{round(tester.download() /(10**6))} Mbps'
        return download


    def upload(self):
        tester = self.tester
        upload = f'{round(tester.upload() /(10**6))} Mbps'
        return upload

        
def check():
    while True:
        t = Test(tester)
        u=t.upload()
        d=t.download()
        print('done')
        return u,d
        
        


'''print('!!!!!!!\nThis will take a moment\n!!!!!!!')
t = threading.Thread(target=check)
t.start()'''

