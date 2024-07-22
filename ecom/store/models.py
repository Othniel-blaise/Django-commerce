from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User,auto_now_add=True)
    phone = models.CharField(max_length=20 ,blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    contry = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username 
 # create a user Profile bye default when user signs up
def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)         
        



# Category of Products
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Meta:
    verbose_name_plural = 'categories'        

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__ (self):
        return f'{self.first_name} {self.last_name}'


# all of our Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=3, max_digits=10 )
    category = models.ForeignKey(Category, on_delete= models.CASCADE,default=1)
    description = models.CharField(max_length=250,default='', blank=True,null=True)
    image = models.ImageField(upload_to ='uploads/product/')
#  Add sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=3, max_digits=10 )   


    def __str__(self):
        return self.name


# Customer Orders
class Order(models.Model): 
    product = models.ForeignKey(Product , on_delete =models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1 )
    address = models.CharField(max_length=100, default='', blank=True )
    phone = models.CharField(max_length=20, default='', blank=True ) 
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product   

