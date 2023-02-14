
from email import message
from django.contrib import messages
from django.http import HttpResponse , HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth


def login(request):
    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']

        user =auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentionl')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# Create register model here.
def register(request):

    if request.method == 'POST':

        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email = request.POST['email']

        if password1==password2:
                # check the username is allredy exist or not
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username taken")
                    return redirect('/')
                # check the email is allredy exist or naot    
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"email taken")
                    return redirect('/')
                else:
                    #create obj(user) for postgres db
                    user =User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.info(request,"user created")
                    return redirect('login')
        else:
           messages.info(request,"password dos not match")
        return redirect('/')
    else:
        return render(request,'register.html')
        
# creating login action here.

