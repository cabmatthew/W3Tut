from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('main')
        else:
            messages.success(request, ("There was an error logging in . . . Try again."))
            return redirect('login')

    else:
        # {}: context dictionary of nothing
        return render(request, 'authenticate/login.html', {})
    
def no_login(request):
    template = loader.get_template('authenticate/nologin.html')
    return HttpResponse(template.render())
