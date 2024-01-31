from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from shoppingapp.models import Schedule, User, Appointment, shopkeeper


@login_required(login_url='login')
def user_home(request):
    return render(request, 'userpage/user_home.html')


@login_required(login_url='login')
def schedule_user(request):
    s = Schedule.objects.all()
    context = {
        'schedule': s
    }
    return render(request, 'userpage/schedule.html', context)


@login_required(login_url='login')
def take_appointment(request, id):
    s = Schedule.objects.get(id=id)
    u = User.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u, schedule=s)
    if appointment.exists():
        messages.info(request, 'you have already requested appointment for this schedule')
        return request('schedule')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = u
            obj.schedule = s
            obj.save()
            messages.info(request, 'Appointment Booked')
            return redirect('appointment_view')
    return render(request, 'userpage/take_appointment.html', {'s': s})


@login_required(login_url='login')
def view_appointment(request):
    u = User.objects.get(user=request.user)
    a = Appointment.objects.filter(user=u)
    return render(request, 'userpage/view_appointment.html', {"a": a})


def shopenter(request):
    return render(request, 'userpage/shopenter.html')


@login_required(login_url='login')
def shop_view(request):
    s = shopkeeper.objects.all()
    context = {
        'shop': s
    }
    return render(request, 'userpage/shoplist.html', context)
