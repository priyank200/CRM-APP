from django.db import models
from django.contrib.auth.models import User

class Leads(models.Model):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    
    CHOICES_PRIORITY = (
        (LOW,"Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High")
    )
    
    NEW = "new"
    CONTACTED = "contacted"
    WON = "won"
    LOST = "lost"
    
    CHOICES_STATUS = (
        (NEW, "New"),
        (CONTACTED, "Contacted"),
        (WON, "Won"),
        (LOST, "Lost")        
    )
        
    name = models.CharField(max_length=25)
    email = models.EmailField()
    description = models.TextField(blank=True,null=True)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name