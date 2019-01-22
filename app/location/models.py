from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=10)
    location_number = models.IntegerField()


class Sub_location(models.Model):
    name = models.CharField(max_length=10)
    location = models.ForeignKey('Location',
                                 on_delete=models.CASCADE,
                                 related_name='sub_location',)
    sub_location_number = models.IntegerField()


class Pensions(models.Model):
    name = models.CharField(max_length=100)
    sub_location = models.ForeignKey('Sub_location',
                                     on_delete=models.CASCADE,
                                     related_name='pension',)
    address = models.TextField(max_length=100),
    check_in = models.CharField(max_length=10),
    check_out = models.CharField(max_length=10),


