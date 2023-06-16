from datetime import datetime

from django.db import models

# Create your models here.
from accounts.models import CustomUser

ROLES = (
    ('client', 'Son Kullanıcı'),
    ('partner', 'İş Ortağı'),
)

POC_REQUEST = (
    (1, 'Toplantı Aşaması'),
    (2, 'POC Talebi'),
    (3, 'POC Aşaması'),
    (4, 'POC Gerçekleştirildi'),
    (5, 'Yaklaşık Maliyet'),
    (6, 'Alım Aşaması'),
    (7, 'Pazarlık Aşaması'),
    (8, 'Gerçekleşti'),
    (9, 'Kapandı'),
    (10, 'Kaybedildi')
)

NOTES_CATEGORIES = (
    (1, 'Arama'),
    (2, 'Yüzyüze Görüşme'),
    (3, 'İş Ortağı İle Görüşme'),
    (4, 'E-posta'),

)


class Company(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=7, choices=ROLES)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)


class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=255)


class Project(models.Model):
    client = models.ForeignKey(to=Company, related_name="client", on_delete=models.CASCADE)
    partner = models.ForeignKey(to=Company, related_name="partner", on_delete=models.CASCADE, null=True, blank=True)
    registration_date = models.DateField(auto_now=True)
    exp_end_date = models.DateField(null=True, blank=True)
    tender_date = models.DateField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    count = models.IntegerField()
    client_contact = models.ForeignKey(to=People, related_name="client_contact", on_delete=models.CASCADE, null=True, blank=True)
    partner_contact = models.ForeignKey(to=People, related_name="partner_contact", on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    budget = models.FloatField()
    poc_request = models.CharField(max_length=1, choices=POC_REQUEST)
    probability = models.CharField(max_length=3)
    registered_by = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT)


class Notes(models.Model):
    title = models.CharField(max_length=255)
    note = models.TextField()
    creation_date = models.DateField(auto_now=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    category = models.CharField(max_length=1, choices=NOTES_CATEGORIES)



class FinishedProject(models.Model):
    invoice_date = models.DateField()
    invoice_amount = models.IntegerField()
    end_date = models.DateField(default=datetime.now, blank=True)
    client = models.ForeignKey(to=Company, related_name="finished_client", on_delete=models.CASCADE)
    partner = models.ForeignKey(to=Company, related_name="finished_partner", on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    budget = models.FloatField()
    count = models.IntegerField()
    agreement = models.FileField(upload_to='sözlesmeler/', null=True, blank=True)
    registered_by = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT)


