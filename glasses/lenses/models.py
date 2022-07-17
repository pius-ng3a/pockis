from tabnanny import verbose
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True) # used for url generation
    class Meta:
        verbose_name_plural = "categories" #Django should use this as plural form of category instead of categorys
    def get_absolute_url(self):
        return reverse("glass:category_list", args=[self.slug])
    def __str__(self) -> str:
        return self.name
    
class Glass(models.Model):
    #glass_id = #unique identifier
    name = models.CharField(max_length =100)
    category = models.ForeignKey(Category,related_name="glass", on_delete=models.CASCADE) # the type of glass
    size = models.IntegerField()#the size of the glass
    stock = models.IntegerField()#number available
    color = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="glass_creator")
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    is_active = models.BooleanField(default=True) # are you currently selling the product or not
    avatar = models.ImageField(upload_to="images/") #image of the object
    slug = models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True) #date created
    updated = models.DateTimeField(auto_now=True) #date updated
    
    class Meta:
        verbose_name_plural ="glasses"
        ordering = (['-created']) # how the items are sorted when fetched
    def __str__(self): #string method for the class
        return self.name

class Order(models.Model):
    order_number = models.CharField(max_length=100,primary_key=True)
    is_paid =  models.BooleanField(default=False) #paid or not
    user_id = models.ForeignKey(User,on_delete=models.CASCADE) # Currently logged in user id from session 
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated

    def __str__(self) -> str:
        return self.order_number
    
class OrderItem(models.Model): # holds  the  various items in the order
    order_number = models.ForeignKey(Order,on_delete=models.CASCADE)# references order
    glass_id = models.ForeignKey(Glass,on_delete=models.CASCADE)# particular glass ordered
    quantity = models.IntegerField()# number ordered
    created  = models.DateTimeField(auto_now_add=True)# date created
    updated  = models.DateTimeField(auto_now=True) # date updated

class Distributor(models.Model):
    DIST_CHOICES = ( ("Basic (<2000)","Basic (<2000)"),
     ("Medim(<5000)","Medim(<5000)"), ("Premium(>6000)","Premium(>6000)")

    )
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    distributor_type = models.CharField(max_length=100, choices=DIST_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

     
