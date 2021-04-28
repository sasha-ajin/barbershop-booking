from django.db import models


class Time(models.Model):
    tm = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.tm


class Barber(models.Model):
    name = models.CharField(max_length=100, null=True)
    photo = models.ImageField(null=True, blank=True)
    time = models.ManyToManyField(Time,  blank=True)

    def __str__(self):
        return self.name

    @property
    def free(self):
        free = True
        if self.time.count() == Time.objects.count():
            free = False
        return free


class Order(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE,null=True)
    tm = models.ForeignKey(Time, on_delete=models.CASCADE,null=True)
    client_tel = models.CharField(max_length=100, null=True)
    client_name = models.CharField(max_length=100, null=True)
    client_email = models.EmailField()

    def __str__(self):
        return str(self.tm)
