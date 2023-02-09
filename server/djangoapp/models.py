from django.db import models
from django.utils.timezone import now


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='audi')
    description = models.CharField(
        null=False, max_length=200, default='car description')

    def __str__(self):
        return self.name + ": " + self.description


# Car model
class CarModel(models.Model):
    model_name = models.CharField(max_length=200, default="title")
    description = models.ForeignKey(
        CarMake, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    year = models.DateField()
    dealer_id = models.IntegerField()

    def __str__(self):
        return "Model: " + self.model_name + "," + \
            "Description: " + self.description


class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


class DealerReview:

    def __init__(self, dealership, purchase, name, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.purchase = purchase
        self.name = name
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id

    def __str__(self):
        return "Dealer name: " + self.full_name
