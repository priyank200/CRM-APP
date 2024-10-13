from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

# Create your views here.
def signup(request):    
    if(request.method == 'POST'):
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            # print("Form is Valid")
            return redirect('log-in')
    else:
        form  = UserCreationForm()
        
    return render(request,'userprofile/signup.html', {
        'form':form
    })