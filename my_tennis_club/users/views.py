from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

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

def logout_user(request):
    logout(request)
    messages.success(request, ("You've been logged out!"))
    return redirect('main')

def register_user(request):
    # if someone filled out the form, do something
    if request.method == "POST":
        # if user filled out the form, pass the POST in to UserCreationForm
        form = UserCreationForm(request.POST)
        # validate the form
        if form.is_valid():
            # save their information
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # register & login/authenticate
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration successful!'))
            return redirect('main')
        
    # show the form if not yet filled out
    else:
        # don't pass in the POST, user hasn't filled form out yet
        form = UserCreationForm()

    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })