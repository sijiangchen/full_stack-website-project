from django.shortcuts import render
from django.http import HttpResponse
# from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.


# def index(request):
#     return HttpResponse("<em>My Second Project</em>")

def welcome(request):
    # welcomedict={'welcome_insert':'Go to /users to see the list of user information!'}
    return render(request,'welcome.html')

def users(request):
    # users_list=User.objects.all()
    # user_dict={'users':users_list}
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return welcome(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,"users.html",{'form':form})
