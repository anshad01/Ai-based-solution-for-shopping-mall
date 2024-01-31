from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from shoppingapp.forms import SchdeuleForm
from shoppingapp.models import Schedule, Appointment


@login_required(login_url='login')
def shopkeeper_home(request):
    return render(request, 'shopkeeperpage/shopkeeper_home.html')


@login_required(login_url='login')
def schedule_add(request):
    form = SchdeuleForm()
    if request.method == 'POST':
        form = SchdeuleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'schedule added successful')
            return redirect('schedule_views')
    return render(request, 'shopkeeperpage/schedule_add.html', {'form': form})


@login_required(login_url='login')
def schedule_view(request):
    s = Schedule.objects.all()
    context = {
        'schedule': s
    }
    return render(request, 'shopkeeperpage/schedule_view.html', context)


@login_required(login_url='login')
def schedule_update(request, id):
    s = Schedule.objects.get(id=id)
    if request.method == 'POST':
        form = SchdeuleForm(request.POST or None, instance=s)
        if form.is_valid():
            form.save()
            messages.info(request, 'schdeule updated')
            return redirect('schedule_views')
    else:
        form = SchdeuleForm(instance=s)
    return render(request, 'shopkeeperpage/schedule_update.html', {'form': form})


@login_required(login_url='login')
def schedule_delete(request, id):
    s = Schedule.objects.filter(id=id)
    if request.method == 'POST':
        s.delete()
        return redirect('schedule_views')

def appointment_section(request):
    a = Appointment.objects.all()
    context = {
        'appointment': a
    }
    return render(request, 'shopkeeperpage/appointment.html', context)



