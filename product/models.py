from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("카테고리명",max_length=50)

    def __str__(self):
        return self.name

class CoffeeMachine(models.Model):
    brand = models.CharField("커피머신 브랜드", max_length=100)

    def __str__(self):
        return self.brand

class Product(models.Model): #커피캡슐
    seller = models.ForeignKey('user.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    machine = models.ForeignKey(CoffeeMachine, on_delete=models.CASCADE)
    name = models.CharField("캡슐이름", max_length=100)
    explain = models.TextField("캡슐설명")
    thumbnail = models.FileField(upload_to='product/thumbnail')
    detali_img = models.FileField(upload_to='product/detail')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


