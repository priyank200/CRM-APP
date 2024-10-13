from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required # If I a not login the I will be redirect to login page
def dashboard(request):
    return render(request,'dashboard/dashboard.html')