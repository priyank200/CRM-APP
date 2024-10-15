from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm
from .models import Leads
from django.contrib import messages

# model of client
from client.models import Client


@login_required
def leads_list(request):
    leads = Leads.objects.filter(created_by=request.user)
    
    return render(request,'lead/leads_list.html',{
        'leads':leads
    })


@login_required
def lead_details(request,pk):
    # lead = Leads.objects.filter(created_by=request.user).get(pk=pk) # here we have to use filter because user should only see there own lead not anyone leads
    #Another way to get the details
    lead = get_object_or_404(Leads,created_by=request.user,pk=pk)
    return render(request,'lead/lead_details.html',{
        "lead":lead
    })
    


# Create your views here.
@login_required
def add_lead(request):
    if request.method == "POST":
        form = AddLeadForm(request.POST)
        if form.is_valid():
            # commit=False: The form creates an instance of the model, but does not save it to the database right away.
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(request,"Lead is successfully added")
            return redirect('leads-list')              
    else:
        form = AddLeadForm()
    return render(request,'lead/add_lead.html', {'form':form})



@login_required
def edit_lead(request, pk):
    lead = get_object_or_404(Leads,created_by=request.user,pk=pk)
    
    if request.method == "POST":
        form = AddLeadForm(request.POST,instance=lead)
        
        if form.is_valid():
            form.save()
            messages.success(request,"Lead is successfully updated")
            return redirect('leads-list')
        else:
            print("Failed")
            messages.warning(request,"Form is invaild")
            
    else:
        form = AddLeadForm(instance=lead)
        
    return render(request,'lead/edit_lead.html', {'form':form})

    

@login_required
def delete_lead(request,pk):
     lead = get_object_or_404(Leads,created_by=request.user,pk=pk)
     lead.delete()
     messages.success(request,"Lead is successfully deleted")
     return redirect('leads-list')
 
@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Leads,created_by=request.user,pk=pk)
    client = Client.objects.create(
                    name = lead.name,
                    email = lead.email,
                    description=lead.description,
                    created_by = request.user
                    )
    
    lead.converted_to_client = True
    lead.save()
    messages.success(request,"Lead is successfully converted to client")
    
    return redirect('leads-list')