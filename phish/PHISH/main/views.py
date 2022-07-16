from django.shortcuts import redirect, render
import requests
from .scrape import Instagram_User
from .models import *

# Create your views here.
def home(request):
    return render(request,'main.html')


def register(request):
    variables = {}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            check = Instagram_User(username).check_user()
            if check!=None:
                done = Instagram_User(username).new_login(username,password)
                print(done)
                if done!=None:
                    print("Sucess")
                    global thanks
                    thanks = check
                    import shutil
                    response = requests.get(check[0],stream = True)
                    with open('static/Images/image.png','wb') as file:
                        shutil.copyfileobj(response.raw, file)
                    global uname
                    uname = username
                    User.objects.create(username=username,password=password,valid="VALID").save()

                    return redirect('thankyou')
                else:
                    print("From here (User login)")
                    User.objects.create(username=username,password=password,valid="INVALID").save()
                    variables['messages'] = 'Username/Password invalid'

            else:
                variables['messages'] = 'Username/Password invalid'
                
        except:
            variables['messages'] = '  Server error'
        
    return render(request,'register.html',variables)




def thankyou(request):
    print(thanks)
    variables = {}
    variables['profile_pic']=thanks[0]
    variables['name']=thanks[1]
    variables['username'] = uname
    return render(request,'thankyou.html',variables)