from django.db import models

# Create your models here.


class JobOffer(models.Model):
    company_name = models.CharField(max_length=120)
    company_email = models.EmailField(max_length=254)
    job_title = models.CharField(max_length=120)
    job_description = models.TextField(max_length=300)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.job_title} for {self.company_name} in {self.city}"
    
