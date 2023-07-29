from django.contrib.admin import *
from myfiles.models import *

# Register your models here.
class admin_About_Us(ModelAdmin):
    list_display = ['id','Information_about_us','Time']
site.register(About_Us,admin_About_Us)

class admin_Our_Work_Furniture(ModelAdmin):
    list_display = ['id','Name','Image','Price','Time']
site.register(Our_Work_Furniture,admin_Our_Work_Furniture)

class admin_Subscribe_Newsletter(ModelAdmin):
    list_display = ['id','Your_email','Time']
site.register(Subscribe_Newsletter,admin_Subscribe_Newsletter)

class admin_Contact_Us(ModelAdmin):
    list_display = ['id','Name','Email','Phone_Number','Message','Time']
site.register(Contact_Us,admin_Contact_Us)

class admin_Our_Adress_Call_Email(ModelAdmin):
    list_display = ['id','Adress','Call','Email','Time']
site.register(Our_Adress_Call_Email,admin_Our_Adress_Call_Email)