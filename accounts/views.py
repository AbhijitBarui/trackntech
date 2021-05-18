from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from interests.models import Interest

def register(request):
    if request.method == "POST":
        #Register user logic
        #get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #password cross-check
        if password == password2:
            #check Username availability
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            else:
                #Check E-mail Relations
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'E-mail is already linked to an account')
                    return redirect('login')
                else:
                    #register begin
                    user = User.objects.create_user(
                        username = username,
                        password = password,
                        email = email,
                        first_name = first_name,
                        last_name = last_name,
                    )
                    #auto login after registration successful
                    #auth.login(request, user)
                    #messages.success(request, 'You are now logged in')
                    #return redirect('index')

                    #manual login
                    user.save()
                    messages.success(request, 'You are now registered with us')
                    return redirect('login')
        else:
            messages.error(request, 'passwords entered do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == "POST":
        #Login user logic
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'you are successfully logged out')
        return redirect('index')


def dashboard(request):
    user_interests = Interest.objects.order_by('-interest_date').filter(user_id=request.user.id)
    context = {
        'interests': user_interests
    }
    return render(request, 'accounts/dashboard.html', context)
