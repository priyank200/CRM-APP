from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Client


@login_required
def clients_list(request):
    clinets = Client.objects.filter()
    print(clinets)
    return render(request,'client/client_list.html',{
        'clients':clinets
    })