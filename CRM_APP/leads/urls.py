from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("add-lead/", view=views.add_lead, name='add-lead'),
    path("leads-list/", view=views.leads_list, name='leads-list'),
    path("<int:pk>/", view=views.lead_details,name='lead-details'),
    path('<int:pk>/delete/', view=views.delete_lead, name = 'delete-lead'),
    path("<int:pk>/edit-lead/", view=views.edit_lead,name="edit-lead")
]