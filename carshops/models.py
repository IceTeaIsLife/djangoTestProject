from django.db import models


class Manufacturer(models.Model):
    name = models.TextField()
    country = models.TextField()


class Mark(models.Model):
    name = models.TextField()
    manufacturerID = models.ForeignKey("Manufacturer", on_delete=models.SET_NULL, null=True)


class Shop(models.Model):
    name = models.TextField()


class Stock(models.Model):
    shopID = models.ForeignKey("Shop", on_delete=models.SET_NULL, null=True)
    markID = models.ForeignKey("Mark", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()


