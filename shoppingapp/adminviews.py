from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from shoppingapp.forms import LoginRegister, shopkeeperRegister
from shoppingapp.models import shopkeeper, User, Login, Appointment


@login_required(login_url='login')
def admin_home(request):
    return render(request, 'admintemp/admin_home.html')


@login_required(login_url='login')
def shopkeeper_registery(request):
    user_form = LoginRegister()
    shopkeeper_form = shopkeeperRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        shopkeeper_form = shopkeeperRegister(request.POST)
        if user_form.is_valid() and shopkeeper_form.is_valid():
            user = user_form.save(commit=False)
            user.is_shopkeeper = True
            user.save()
            shopkeeper = shopkeeper_form.save(commit=False)
            shopkeeper.user = user
            shopkeeper.save()
            messages.info(request, 'shopkeeper Registered Successfully')
            return redirect('shopkeeper_views')
    return render(request, 'admintemp/shopkeeper_register.html',
                  {'user_form': user_form, 'shopkeeper_form': shopkeeper_form})


@login_required(login_url='login')
def view_shopkeeper(request):
    s = shopkeeper.objects.all()
    context = {
        'shopkeeper': s
    }
    return render(request, 'admintemp/view_shopkeeper.html', context)


@login_required(login_url='login')
def update_shopkeeper(request, id):
    s = shopkeeper.objects.get(id=id)
    l = Login.objects.get(shop=s)

    if request.method == 'POST':
        form = shopkeeperRegister(request.POST or None, instance=s)
        user_form = LoginRegister(request.POST or None, instance=l)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            messages.info(request, 'schdeule updated')
            return redirect('shopkeeper_views')
    else:
        form = shopkeeperRegister(instance=s)
        user_form = LoginRegister(instance=l)
    return render(request, 'admintemp/update_shopkeeper.html', {'form': form, 'user_form': user_form})


@login_required(login_url='login')
def delete_shopkeeper(request, id):
    u = shopkeeper.objects.get(id=id)
    print(u)
    print(id)
    s = Login.objects.get(shop=u)
    print(s)
    if request.method == 'POST':
        s.delete()
        return redirect('shopkeeper_views')
    else:
        return redirect('shopkeeper_views')


@login_required(login_url='login')
def view_user(request):
    u = User.objects.all()
    context = {
        'user': u
    }
    return render(request, 'admintemp/view_user.html', context)


@login_required(login_url='login')
def delete_user(request, id):
    l = User.objects.get(id=id)
    u = Login.objects.get(user=l)
    if request.method == 'POST':
        u.delete()
        return redirect('user_views')
    else:
        return redirect('user_views')


@login_required(login_url='login')
def appointment_admin(request):
    a = Appointment.objects.all()
    context = {
        'appointment': a
    }
    return render(request, 'admintemp/appointment.html', context)



@login_required(login_url='login')
def approve_appointment(request, id):
    a = Appointment.objects.get(id=id)
    a.status = 1
    a.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_admin')


@login_required(login_url='login')
def reject_appointment(request, id):
    a = Appointment.objects.get(id=id)
    a.status = 2
    a.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_admin')
