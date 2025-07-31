from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.utils.timezone import datetime



from PIL import Image
import os

def resize_image(image_path, max_size=(800, 800)):
    with Image.open(image_path) as img:
        if img.height > max_size[0] or img.width > max_size[1]:
            img.thumbnail(max_size)
            img.save(image_path)

# Create your models here.
class User(AbstractUser):
    is_superuser=models.BooleanField(default=False)
    quantity=models.IntegerField(default=0)
    class Meta:
        db_table='auth_User'
    # def __str__(self):
    #     return self.first_name
    
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    user_image=models.ImageField(upload_to='image',default=False)
    contactno=models.CharField(max_length=10)
    location=models.CharField(max_length=100)
    bio=models.CharField(max_length=300,default="")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.first_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.user_image:
            resize_image(self.user_image.path)



class Dresses(models.Model):
    image=models.ImageField(upload_to='image',default=False)
    title=models.CharField(max_length=100)
    dressid=models.IntegerField(primary_key=True)
    price=models.CharField(max_length=120)
    type=models.CharField(max_length=100)
    dress_for=models.CharField(max_length=100)
    dress_size=models.JSONField(default=list)
    description=models.CharField(max_length=200)
    loggeduser=models.EmailField(max_length=254)
    def __str__(self):
        return self.loggeduser
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            resize_image(self.image.path)




class booked(models.Model):
    img=models.ForeignKey(Dresses,on_delete=models.SET_NULL,null=True)
    size=models.CharField(max_length=50)
    # bookeddress=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    pno=models.CharField(max_length=10)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=200)
    status=models.CharField(max_length=100,default="Pay")
    total=models.CharField(max_length=200,default=0)
    Booked_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.img and self.img.image:
            resize_image(self.img.image.path)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dress = models.ForeignKey(Dresses, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.dress.title}"

    
#    email=request.POST.get('email')
#         print(email)
#         print("Hi")
#         user1=request.user
#         user2=User.objects.get(username=email)
#         print(user1,user2)
#         if user1==user2:
#             img=request.FILES['img']
#             name=request.POST.get('name')
#             bio=request.POST.get('bio')
#             # user1=User.objects.get(username=email)
#                     # if user is not None:
#                     #     user1.set(first_name=name,)
#             print(user1,img,name,bio)
#             user2.first_name=name
#             user2.save()
#             profile=profile(user=user2,user_image=img,bio=bio)
#             profile.update()
#         return render(request,'profileedit.html',context)
#     return render(request,'profileedit.html',context)


    