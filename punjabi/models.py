from django.db import models

# Create your models here.
class Room(models.Model):
    nm = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    space = models.CharField(max_length=20)
    guest = models.CharField(max_length=10)
    price = models.CharField(max_length=50)
    img1 = models.FileField(upload_to='room/img1' ,default="")
    img2 = models.FileField(upload_to='room/img2' ,default="")
    img3 = models.FileField(upload_to='room/img3' ,default="")
    img4 = models.FileField(upload_to='room/img4' ,default="")
    img5 = models.FileField(upload_to='room/img5' ,default="")
    img6 = models.FileField(upload_to='room/img6' ,default="")

class Booking(models.Model):
    nm = models.CharField(max_length=80)
    uid = models.CharField(max_length=40)
    no = models.CharField(max_length=15)
    adds = models.CharField(max_length=200)
    rid = models.CharField(max_length=50)
    room_name = models.CharField(max_length=80)
    price = models.CharField(max_length=80)
    startdate = models.CharField(max_length=80)
    enddate = models.CharField(max_length=80)
    payment = models.CharField(max_length=20, default="")
    status = models.CharField(max_length=20, default="")



class Order(models.Model):
    booking_id=models.CharField(max_length=50)
    startdate=models.CharField(max_length=50)
    enddate = models.CharField(max_length=50)
    room_id = models.CharField(max_length=50,default="null")

class Gallery(models.Model):
    nm=models.CharField(max_length=100)
    img=models.FileField(upload_to='gallery',default="")

class Restaurant(models.Model):
    nm = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    price = models.CharField(max_length=100)
    cat = models.CharField(max_length=100)

class Contact(models.Model):
    nm=models.CharField(max_length=50)
    em=models.CharField(max_length=50)
    no=models.CharField(max_length=15)
    sub=models.CharField(max_length=150)
    msg=models.CharField(max_length=500)
