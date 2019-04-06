from django.db import models

# Create your models here.

class Contract(models.Model):
    description: models.TextField()
    background: models.TextField()
    required_services: models.TextField()
    contract_personnel: models.TextField()
    response_detail: models.TextField()
    title: models.TextField()