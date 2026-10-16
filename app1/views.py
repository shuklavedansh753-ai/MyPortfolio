
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(
                request,
                'Thank you! Your message has been saved.'
            )
        else:
            messages.error(
                request,
                'Please fill in all fields.'
            )

    return redirect('/#contact')
