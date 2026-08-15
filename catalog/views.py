from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def home(request) -> HttpResponse :
    return render(request, "home.html")

def contacts(request) -> HttpResponse :
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')


        if all([name, phone, message]):
            print(f'You have new message from {name}({phone}): {message}')
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('catalog:contacts')  # PRG-паттерн
        else:
            messages.error(request, 'Пожалуйста, заполните все поля')


    return render(request, "contacts.html")