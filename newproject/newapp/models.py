from django.db import models

# Create your models here.
class Car(models.Model):
    FUEL_TYPE= [
        ('source ', 'Select One'),
        ('gas','Gas'),
        ('diesel','Diesel'),
        ('hybrid','Hybrid'),
        ('lp_gas','LP Gas'),
    ]

    ROOF_TYPE=[
         ('select_one', 'Select One'),
        ('solid','Solid'),
        ('sun_roof','Sun Roof'),
        ('convertable','Convertable'),

    ]
    vin = models.CharField(max_length=20)
    make = models.CharField(max_length=100)
    model= models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    roof_type = models.CharField(choices= ROOF_TYPE, default = 'Select One' )
    fuel_type = models.CharField(choices= FUEL_TYPE, default = 'Select One')

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
