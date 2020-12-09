from django.db import models

# Create your models here.
<<<<<<< HEAD
class Cookie(models.Model):
    cookie_name = models.CharField(max_length=30)
    thumbnail = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)

class Club(models.Model):
    club_name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    fundraiser = models.ManyToManyField(Cookie, through="ClubFundraiser")

class ClubFundraiser(models.Model):
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

=======
>>>>>>> 8e84c00699151a5474dccdb482380b03d4ea421e
