from django.db import models

# Create your models here.
ROLES = (
    ('client', 'Son Kullanıcı'),
    ('partner', 'İş Ortağı'),
)

POC_REQUEST = (
    ('Y', 'Evet'),
    ('N', 'Hayır'),
)


class Company(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=7, choices=ROLES)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)


class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=255)


class Project(models.Model):
    client = models.ForeignKey(to=Company, related_name="client", on_delete=models.CASCADE)
    partner = models.ForeignKey(to=Company,related_name="partner", on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now=True)
    exp_end_date = models.DateField()
    tender_date = models.DateField()
    info = models.TextField()
    status = models.CharField(max_length=10)
    count = models.IntegerField()
    client_contact = models.ForeignKey(to=People,related_name="client_contact", on_delete=models.CASCADE)
    partner_contact = models.ForeignKey(to=People,related_name="partner_contact", on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    budget = models.FloatField()
    poc_request = models.CharField(max_length=1, choices=POC_REQUEST)
    probability = models.CharField(max_length=3)



