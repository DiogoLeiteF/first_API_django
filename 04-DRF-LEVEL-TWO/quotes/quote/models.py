from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Quote(models.Model):
    quote_author = models.CharField(max_length=60, blank=False, null=False)
    quote_body = models.TextField(null=False)
    context = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=100, blank=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.quote_body}, by {self.quote_author}"
    
    
    