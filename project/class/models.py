from django.db import models
from django.conf import settings


class Class(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()

    def get_absolute_url(self):
        return '../../../'

    def __str__(self):
        return self.name + "    ~    " + str(self.code)


class RedemptionPage(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)


class Item(models.Model):
    RedemptionPage = models.ForeignKey(RedemptionPage, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def get_absolute_url(self):
        return '../'

    def __str__(self):
        return 'Item: ' + self.name + ' ~ Points: ' + str(self.price)



class Assignment(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    points_value = models.IntegerField()

    def get_absolute_url(self):
        return '../'

    def __str__(self):
        return self.name + ' ' + self.description + ' ' + str(self.points_value)


class Student_Class(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Calendar(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    event = models.CharField(max_length=10000)

    def get_absolute_url(self):
         return '../'

    def __str__(self):
         return self.event