from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.mail import send_mail
from .models import EventAdvisor, PartiesEvent, CollegeEvent, WeddingEvent, Contact, TechnicalEvent


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def technicalevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date =  request.POST.get('date')
        time =  request.POST.get('time')
        guest =  request.POST.get('guest')
        technicalevent = EventAdvisor(name=name, email=email, phone=phone, destination=destination,date = date,time = time,guest = guest, desc =desc)
        technicalevent.save()
        return render(request,'technicalsuccess.html',{'event':"technicalevent",'date':date,'destination':destination})
    return render(request,'technicalevent.html')


@login_required(login_url='login')
def partiesevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        guest = request.POST.get('guest')

        # Convert date and time strings to datetime objects
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        time = datetime.strptime(time_str, '%H:%M').time()

        partiesevent = PartiesEvent(name=name, email=email, phone=phone, destination=destination, date=date, time=time,
                                    guest=guest, desc=desc)
        PartiesEvent.save()

        return render(request,'technicalsuccess.html',{'event':"partiesevent",'date':date,'destination':destination})

    return render(request, 'partiesevent.html')


@login_required(login_url='login')
def collegeevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guest = request.POST.get('guest')
        collegeevent = CollegeEvent(name=name, email=email, phone=phone, destination=destination, date=date, time=time,
                                    guest=guest, desc=desc)
        collegeevent.save()
        return render(request,'technicalsuccess.html',{'event':"collegeevent",'date':date})

    return render(request, 'collegeevent.html')





@login_required(login_url='login')
def weddingevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        guest = request.POST.get('guest')

        # Convert date and time strings to datetime objects
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        time = datetime.strptime(time_str, '%H:%M').time()

        weddingevent = WeddingEvent(name=name, email=email, phone=phone, destination=destination, date=date, time=time,
                                    guest=guest, desc=desc)
        weddingevent.save()

        return render(request, 'technicalsuccess.html', {'event': "collegeevent", 'date': date,'destination':destination})

    return render(request, 'weddingevent.html')


@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        send_mail(
            'Feedback Form',
            'Thank you for Using eventmanagement System',
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False)
        try:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.now())
            contact.save()
            messages.success(request, 'Your message has been sent!')
        except Exception as e:
            messages.error(request, f'Error occurred: {e}')
    return render(request, 'contact.html')
def services(request):
    return render(request,'services.html')
def success(request):
    return render(request,'success.html')
def technicalsuccess(request):
    return render(request,'technicalsuccess.html')
def index(request):
    technical=TechnicalEvent.objects.all()
    return render(request,'index.html',{'technical':technical})

