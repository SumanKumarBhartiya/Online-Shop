from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id = models.AutoField
    Product_name = models.CharField(max_length=30)
    Category=models.CharField(max_length=50,default="")
    Sub_category=models.CharField(max_length=50,default="")
    Price=models.IntegerField(default="0")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    Prod_image=models.ImageField(upload_to="Shop/images",default="")

    def __str__(self):
        return self.Product_name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)

    def __str__(self):
        return self.name
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."