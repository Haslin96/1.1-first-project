from django.shortcuts import render
from phones.models import Phone

def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'phone_list.html', {'phones': phones})

def phone_detail(request, slug):
    phone = Phone.objects.get(slug=slug)
    return render(request, 'phone_detail.html', {'phone': phone})