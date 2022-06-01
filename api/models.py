from django.db import models

# Create your models here.
class Images(models.Model):
    _id = models.BigAutoField(primary_key=True)
    img_url = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label
