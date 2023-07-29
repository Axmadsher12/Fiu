from django.db.models import *

# Create your models here.
class About_Us(Model):
    Information_about_us = TextField(null=True,blank=True)
    Time = DateTimeField(null=True,blank=True,auto_now_add=True)

class Our_Work_Furniture(Model):
    Name = CharField(max_length=25,null=True,blank=True)
    Image = ImageField(upload_to='Media',null=True,blank=True)
    Price = IntegerField(null=True,blank=True)
    Time = DateTimeField(null=True,blank=True,auto_now_add=True)

class Subscribe_Newsletter(Model):
    Your_email = EmailField(null=True,blank=True)
    Time = DateTimeField(null=True,blank=True,auto_now_add=True)

class Contact_Us(Model):
    Name = CharField(max_length=25,null=True,blank=True)
    Email = EmailField(null=True,blank=True)
    Phone_Number = IntegerField(null=True,blank=True)
    Message = TextField(null=True,blank=True)
    Time = DateTimeField(null=True,blank=True,auto_now_add=True)

class Our_Adress_Call_Email(Model):
    Adress = TextField(null=True,blank=True)
    Call = IntegerField(null=True,blank=True)
    Email = EmailField(null=True,blank=True)
    Time = DateTimeField(null=True,blank=True,auto_now_add=True)


# null=True,blank=True