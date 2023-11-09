from django.db import models

# Create your models here.



class Journalist(models.Model):
    first_mame = models.CharField(max_length=60)
    last_mame = models.CharField(max_length=60)
    biogrhaphy = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.first_mame} {self.last_mame}"


class Article(models.Model):
    # author = models.CharField(max_length=50)
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{ self.author} {self.title}"