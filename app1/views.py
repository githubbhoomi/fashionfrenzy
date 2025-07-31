from django.shortcuts import render,redirect
from .models import *
# from django.contrib.auth.models import User
from django.db.models import Max
from django.contrib import messages
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate,logout
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import datetime




# Create your views here.
def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        pas1=request.POST.get('psw1')
        pas2=request.POST.get('psw2')
        pno=request.POST.get('cno')
        location=request.POST.get('location')
        img=request.FILES['image']
        if pas1!=pas2:
            messages.success(request,"Password does not match")
            return render(request,'registration.html')
        elif User.objects.filter(username=email).first():
            messages.success(request,"email is already taken")
            return render(request,'registration.html')
        else:
                user=User.objects.filter(username=email).first()
                if  user is None:
                    user_obj=User.objects.create_user(username=email,email=email,password=pas1,is_superuser=False)
                    user_obj.first_name=name
                    user_obj.save()
                    profile_obj=profile(user=user_obj,user_image=img,contactno=pno,location=location)
                    profile_obj.save()
                    messages.success(request,f"{name} Registered successfully")
                    return render(request,'registration.html')
                else:
                    # user_obj=User.objects.create_user(username=email,email=email,password=pas1,is_super=False)
                    # user_obj.first_name=name
                    # user_obj.save()
                    # profile_obj=profile(user=user_obj,user_image=img)
                    # profile_obj.save()
                    messages.success(request,f"{name} was already Registered")
                    return render(request,'register.html')
    return render(request,'registration.html')

def login(request):
    if request.method=="POST":
        # name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        # user_obj=User.objects.get(email=mail)
        # print(user_obj)
        user=authenticate(username=email,email=email,password=password)
        print(user)
        if user is not None:
            if user.is_superuser==True:
                print(user,"hi","super")
                django_login(request,user)
                dress=booked.objects.all()
                dresses=dress.count()
                print(dresses)
                logu=profile.objects.all()
                loguser=logu.count()
                print(loguser)
                context={'total_dresses_booked':dresses,'users_logged_in':loguser}
                return render(request,'superuser.html',context)
            else: 
                print("not super")
                django_login(request,user)
                return render(request,'home.html')
        else:
            print("out")
            return render(request,'home.html')
    return render(request,'home.html')

def category(request,type=None):
    if request.method=="POST":
        dress=Dresses.objects.filter(type=type)
        context={"dresses":dress}
        return render(request,'women.html',context)
    return render(request,'women.html')









def men(request):
    dress=Dresses.objects.filter(dress_for="men")
    context={"dresses":dress}
    return render(request,'men.html',context)

def women(request):
    dress=Dresses.objects.filter(dress_for="women")
    context={"dresses":dress}
    return render(request,'women.html',context)

def kids(request):
    dress=Dresses.objects.filter(dress_for="kids")
    context={"dresses":dress}
    return render(request,'kids.html',context)

def mentypeofdress(request):
    try:
        if request.method=="POST":
            k=request.POST.get('type',"")  
            if 'traditional' in k:
                dress=Dresses.objects.filter(type="traditional",dress_for="men")
            if 'dailywear' in k:
                dress=Dresses.objects.filter(type="dailywear",dress_for="men")
            if 'nightdress' in k:
                dress=Dresses.objects.filter(type="nightdress",dress_for="men")
            if 'partywear' in k:
                dress=Dresses.objects.filter(type="partywear",dress_for="men")
            if 'weddingwear' in k:
                dress=Dresses.objects.filter(type="weddingwear",dress_for="men")
            context={"dresses":dress}
        return render(request,'men.html',context)
    except Exception :
        messages.success(request,"No dress is posted")
        return render(request,'men.html')
           






def womentypeofdress(request):
    # try:
    print("hello")
    if request.method=="POST":
        print("Hi")
        k=request.POST.get('type',"")  
        print(k)
        if 'traditional' in k:
            dress=Dresses.objects.filter(type="traditional",dress_for="women")
        if 'dailywear' in k:
            dress=Dresses.objects.filter(type="dailywear",dress_for="women")
        if 'nightdress' in k:
            dress=Dresses.objects.filter(type="nightdress",dress_for="women")
        if 'partywear' in k:
            dress=Dresses.objects.filter(type="partywear",dress_for="women")
        if 'weddingwear' in k:
            dress=Dresses.objects.filter(type="weddingwear",dress_for="women")
        else:
            dress=Dresses.objects.filter(type="traditional",dress_for="women")
        context={"dresses":dress}
        print(dress)
        return render(request,'women.html',context)
        # else:
        #     return redirect(booking)
    # except Exception :
    #     messages.success(request,"No dress is posted")
    return render(request,'women.html')
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
@login_required
def add_to_cart(request, dress_id):
    user = request.user
    dress = get_object_or_404(Dresses, id=dress_id)

    cart_item, created = Cart.objects.get_or_create(user=user, dress=dress)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')  # Redirects to the cart page
def kidstypeofdress(request):
    try:
        if request.method=="POST":
            k=request.POST.get('type',"")  
            if 'traditional' in k:
                dress=Dresses.objects.filter(type="traditional",dress_for="kids")
            if 'dailywear' in k:
                dress=Dresses.objects.filter(type="dailywear",dress_for="kids")
            if 'nightdress' in k:
                dress=Dresses.objects.filter(type="nightdress",dress_for="kids")
            if 'partywear' in k:
                dress=Dresses.objects.filter(type="partywear",dress_for="kids")
            if 'weddingwear' in k:
                dress=Dresses.objects.filter(type="weddingwear",dress_for="kids")
            context={"dresses":dress}
        return render(request,'kids.html',context)
    except Exception :
        messages.success(request,"No dress is posted")
        return render(request,'kids.html')

def womens(request):
    dress=Dresses.objects.filter(dress_for="women")
    context={"dresses":dress}
    return render(request,'traditional.html',context)

def mens(request):
    dress=Dresses.objects.filter(dress_for="men")
    context={"dresses":dress}
    return render(request,'traditional.html',context)

def kid(request):
    dress=Dresses.objects.filter(dress_for="kids")
    context={"dresses":dress}
    return render(request,'traditional.html',context)

# def kurtha(request):
#     dress=Dresses.objects.filter(type="kurtha")
#     context={"dresses":dress}
#     return render(request,'kurtha.html',context)

# def Partywear(request):
#     dress=Dresses.objects.filter(type="partywear")
#     context={"dresses":dress}
#     return render(request,'Partywear.html',context)

# def Skirt(request):
#     dress=Dresses.objects.filter(type="skirt")
#     context={"dresses":dress}
#     return render(request,'Skirt.html',context)

# def weddingwear(request):
#     dress=Dresses.objects.filter(type="weddingwear")
#     context={"dresses":dress}
#     return render(request,'weddingwear.html',context)


def image(request):
    if True:
        id=1 if  Dresses.objects.count()==0 else Dresses.objects.aggregate(max=Max('dressid'))["max"]+1
        context = {'id':id}
        if request.method=="POST":
            image=request.FILES['image']
            title=request.POST.get('title')
            price=request.POST.get('price')
            type=request.POST.get('type')
            dress_for=request.POST.get('dress_for')
            dress_size=request.POST.getlist('size')
            description=request.POST.get('description')
            user=request.user
            useremail=user.email
            print(user.email)
            all_image=images(dressid=id,image=image,title=title,price=price,type=type,dress_for=dress_for,dress_size=dress_size,description=description,loggeduser=useremail)
            all_image.save()
        # if type=="traditional":
        #     td=tradition(image=image,price=price)
        #     td.save()
        # elif type=="skirt":
        #     td=skirts(image=image,price=price)
        #     td.save()
        # elif type=="saree":
        #     td=tradition(image=image,price=price)
        #     td.save()
        # elif type=="partywears":
        #     td=tradition(image=image,price=price)
        #     td.save()
        # elif type=="weddindwears":
        #     td=tradition(image=image,price=price)
        #     td.save()
        messages.success(request,'Dress inserted successfully')
        return render(request,'image.html',context)
   


def logout1(request):
    logout(request)
    return render(request,'home.html')

def delete1(request):
    dress=Dresses.objects.all()
    context={'dresses':dress}
    return render(request,'delete.html',context)


def deletedress(request):
    if request.method=="POST":
        id=request.POST.get('id')
        print(id)
        dress=Dresses.objects.get(dressid=id)
        print(dress)
        dress.delete()
    return redirect('delete1') 
    # dress=Dresses.objects.filter(dressid=id)
    # if dress is not None:
    #     messages.success(request,f"dress of this {id} deleted successfully")
    #     dress.delete()
    #     # type="Traditional"
    #     # url = reverse('messagelib') + f"?type={type}"
    #     # context = {
    #     # "message": "Dress deleted",
    #     # "url": url
    #     # }
    #     # return render(request, "messagelink.html", context)
    # return render(request, "delete.html" )
    
    
def messagelib(request):
    type = request.GET.get('type')
    dress=Dresses.objects.filter(type=type)
    context={'dress':dress}
    return render(request,'delete.html',context) 
        # print(id)
    # dress=Dresses.objects.get(dressid=id)
    # print(dress)
        # dress.delete()
    # messages.success(request,f"dress of this {id} deleted successfully")
        # return redirect('delete1')
    # return render(request,'delete.html')


    
    
    
# from .helpers import send_forget_password_mail
import random

def forgotpass(request):
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            print(email)
            users=User.objects.filter(username=email,first_name=name)
            if users is None:
                messages.success(request,"No user found with this email")
                return redirect(forgotpass)
            else:
                token= ''.join([str(random.randint(0, 9)) for _ in range(6)])
                print(token)
                user=User.objects.get(email=email)
                # user_profile=profile.objects.get(user=user)
                # print(user_profile,"hi")
                # print("hello")
                # user_profile.save()
                # print(token,email)
                send_forget_password_mail(user,token)
                messages.success(request,"An email sent")
                # return redirect(forgotpass)
                return render(request,'otp.html',{'otp':token,'email':user})
    except Exception as e:
       print(e) 
    return render(request,'forgotpass.html')

def send_forget_password_mail(email , token):
    subject='OTP for changepassword'
    message=f'Hi , Your otp is {token}'
    print(message)
    email_from= settings.EMAIL_HOST_USER
    recipeient_list=[email]
    send_mail(subject,message,email_from,recipeient_list)
    return True


def checkotp(request):
    print("hi")
    if request.method=="POST":
        k=request.POST.get('btn',"")
        gotp=request.POST.get("gotp")
        email=request.POST.get("email")
        print(gotp,"hi",email,k)
        otp = request.POST.get("otp")
        print(otp,gotp)
        if otp==gotp:
            if "b1" in k:
                return render(request,"changepass.html")
            else:
                print(email)
                user1=User.objects.filter(username=email).first()
                if user1 is not None:
                    print("inner")
                    dresses=booked.objects.filter(email=user1)
                    current_date = timezone.now()
                    print(current_date)
                    dresses.filter(Booked_at__lt=current_date - timezone.timedelta(days=1)).delete()
                    total=0
                    for dress in dresses:
                        if dress.img and dress.img.price is not None:
                            total+=int(dress.img.price)
                            print(total)
                            dress.total=total
                            dress.save()
                    # messages.success(request,"Booked")
                    context={'bookings':dresses,'total':total}
                    messages.success(request,'The Dress will be deleted once 30 days done after dress booked')
                    return render(request,'bookedview.html',context)
                return render(request,'bookedview.html')
        else:
            messages.success(request,"OTP does not match..?")
            user=booked.objects.filter(email=email)
            user.delete()
            return render(request,'otp.html')

def otp(request):
    if request.method=="POST":
        email=request.POST.get('email')
        token= ''.join([str(random.randint(0, 9)) for _ in range(6)])
        send_forget_password_mail(email,token)
        messages.success(request,"An otp sent")
                # return redirect(forgotpass)
        return render(request,'otp.html',{'otp':token,'email':email})   
    return render(request,'otp.html')


def changepass(request,token):
    try:
        print(token)
        # context={'user_id':profile_obj.user.email}
        # profile_obj=profile.objects.get(forget_password_token=token)
        # print(profile_obj)
        # context={'user_id':profile_obj.user.email}
        if request.method=="POST":
            new_password=request.POST.get('newpassword')
            confirm_password=request.POST.get('confirmpassword')
            user_id=request.POST.get('email')
            print(user_id)
            
            
            if user_id is None:
                messages.success(request,'No user id found')
                return redirect(f'/changepass/{token}/')
            
            if new_password!=confirm_password:
                messages.success(request,'Both are not equal')
                return redirect(f'/changepass/{token}/')
            
            
            user_obj=User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')
        
    except Exception as e:
        print(e)
    return render(request,'changepass.html')


    
def uprofile(request):
    user=profile.objects.all()
    context={'profiles':user}
    return render(request,'userprofiles.html',context)    
    
def view(request):
    if request.method=="POST":
        email=request.POST.get('email')
        user=User.objects.get(username=email)
        print(user)
        vuser=Dresses.objects.filter(loggeduser=user).first()
        print(vuser)
        if vuser is None:
            messages.success(request,"No any Posts ")
        else:
            print(vuser,user)
            if str(vuser)==str(user):
                img=Dresses.objects.filter(loggeduser=vuser)
                context={'dresses':img}
                return render(request,'view.html',context)
    return render(request,'view.html')
   
def booking(request):
    if request.method=="POST" :
        dressid=request.POST.get('id')
        size=request.POST.get('dress_size')
        print(dressid,"koi",size)
        return render(request,'booking.html',{'id':dressid,'size':size})
    # else:
    #     return redirect('womentypeofdress')
    return render(request,'booking.html')


def sendingotp(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        print(name,email)
        emails=User.objects.filter(username=email,first_name=name)
        if emails is not None:
            print(email)
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            send_forget_password_mail(email,otp)
            # subject='OTP for application'
            # message=f'Hi ,your otp is {otp}'
            # email_from= settings.EMAIL_HOST_USER
            # recipeient_list=[email]
            # send_mail(subject,message,email_from,recipeient_list)
            messages.success(request,"Email sent")
            return render(request, 'otp.html', {'otp': otp,'email':email})
    return render(request,"sendingotp.html")
        
from datetime import date
      
        
def sendotp(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        pno=request.POST.get('pno')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        address=request.POST.get('delivery_address')
        id=request.POST.get('dressid')
        size=request.POST.get('size')
        # current_time = current_datetime.time()
        # date_object = date.fromisoformat(current_datetime)
        print(name,email,pno,city,state,zipcode,address,id)
        dress=Dresses.objects.filter(dressid=id,dress_size=size)
        dress=Dresses.objects.get(dressid=id)
        print("dress")
        user1=User.objects.filter(username=email,first_name=name).first()
        print(user1)
        if user1 is None:
            print("hi")
            user=User.objects.create_user(username=email,email=email,quantity=1)
            user.first_name=name
            user.save()
        else:
            user2=booked.objects.filter(email=email).count()
            print(user2)
            user=User.objects.get(username=email,first_name=name)
            user.quantity=user2+1
            user.save()
            print(user.quantity)
        # print(total)
        # price=dress.price
        # total=str(int(total)+int(price))
        # print(total)
        buyer=booked(img=dress,size=size,name=name,email=email,pno=pno,city=city,state=state,address=address,zipcode=zipcode)
        buyer.save()
        print(buyer.Booked_at)
        print(email,"hello")
        token= ''.join([str(random.randint(0, 9)) for _ in range(6)])
        # user=booked.objects.get(email=email)
        send_forget_password_mail(email,token)
        messages.success(request,"An otp sent")
                # return redirect(forgotpass)
        return render(request,'otp.html',{'otp':token,'email':email})
    
        
   




    
def profileedit(request):
    user=profile.objects.all()
    context={'profiles':user}
    if request.method=="POST":
        print("hello")
        # if 'b1' in k:
        #     email=request.POST.get('email')
        #     print("k")
        #     print("Hi")
        #     user1=request.user
        #     user2=User.objects.get(username=email)
        #     print(email,user1,user2,"hi")

        email=request.POST.get('email')
        print("Hi")
        user1=request.user
        print(user1)
        user2=User.objects.get(username=email)
        print(user2)
        print(user1,user2)
        if user1==user2:
            #img=request.FILES['image']
            user2.first_name=request.POST.get('name')
            user2.profile.bio=request.POST.get('bio')
            user2.profile.location=request.POST.get('location')
            if 'image' in request.FILES:
                user2.profile.user_image=request.FILES['image']
                print(user2.profile.user_image.url)
        # user1=User.objects.get(username=email)
                # if user is not None:
                #     user1.set(first_name=name,)
            # print(user1,name,bio)
        # user1.set(first_name=name,bio=bio,user_image=img)
        user2.save()
        user2.profile.save()
        user=profile.objects.all()
        context={'profiles':user}
        return render(request,'profileedit.html',context)
    return render(request,'profileedit.html',context)


def bookeddress(request):
    user1=request.user
    print(user1)
    user_images=Dresses.objects.filter(loggeduser=user1)
    print(user_images)
    booked_dress_list=[]
    for user_image in user_images:
        booked_dresses = booked.objects.filter(img=user_image)
        booked_dress_list.extend(booked_dresses)
    context={'user_images':user_images,'booked_dresses':booked_dress_list}
    return render(request,'bookeddress.html',context)

def bookedview(request):
    # book=booked.objects.all()
    # context={'bookings':book}
    return render(request,'bookedview.html')
 
from datetime import datetime,timedelta
   
def cancelorpay(request):
    if request.method=="POST":
        k=request.POST.get('btn',"")
        print(k)
        price=request.POST.get('price')
        email=request.POST.get('email')
        if 'b1' in k:
            id = request.POST.get('id')
            email = request.POST.get('email')

            print(id, email)

        # Filter booked dresses by email
            dresses = booked.objects.filter(email=email)

            for book in dresses:
                if book.img and book.img.dressid is not None:
                    print(book.img.dressid, id)
                    print(type(book.img.dressid), type(id))
                    if str(book.img.dressid) == id:  # Convert id to string for comparison
                        print("hi", book.img.dressid, id)
                        book.delete()

            total = 0

        # Recalculate total after deleting the dress
            dresss = booked.objects.filter(email=email)
            for dress in dresss:
                if dress.img and dress.img.price is not None:
                    total += int(dress.img.price)
                    print(total)
                    dress.total = total
                    dress.save()

        # Delete dresses with Booked_at more than 30 days old
            current_date = timezone.now()
            print(current_date)
            dresss.filter(Booked_at__lt=current_date - timezone.timedelta(days=1)).delete()

        # Filter booked dresses again after deletion
            dresses = booked.objects.filter(email=email)

            context = {'bookings': dresses, 'total': total}
            print(context)
            return render(request, 'bookedview.html', context)
        
            # id=request.POST.get('id')
            # email=request.POST.get('email')
            # print(id,email)
            # books=booked.objects.filter(email=email)
            # for book in books:
            #     if book.img and book.img.dressid is not None:
            #         print(book.img.dressid,id)
            #         print(type(book.img.dressid),type(id))
            #         if id in books and book.img.dressid==int(id):
            #             print("hi",book.img.dressid,id)
            #             book.delete()
            #             dresses=booked.objects.filter(email=email)
            #             total=0
            #             for dress in dresses:
            #                 if dress.img and dress.img.price is not None:
            #                     total+=int(dress.img.price)
            #                     print(total)
            #                     dress.total=total
            #                     dress.save()
            #             for booked_date in dresses:
            #                 print("hi")
            #                 current_date=datetime.now()
            #                 print(current_date)
            #                 if booked_date.Booked_at-current_date==30:
            #                     booked_date.delete()
            #             dress=booked.objects.filter(email=email)
            #             context={'bookings':dress,'total':total}
            #             print(context)
            #             return render(request,'bookedview.html',context)
            #     # return render(request,'bookedview.html')
            #from django.utils import timezone  # Import timezone for datetime operations

# ...

    # if 'b1' in k:
    #     id = request.POST.get('id')
    #     email = request.POST.get('email')

    #     print(id, email)

    #     # Filter booked dresses by email
    #     dresses = booked.objects.filter(email=email)

    #     for book in dresses:
    #         if book.img and book.img.dressid is not None:
    #             print(book.img.dressid, id)
    #             print(type(book.img.dressid), type(id))
    #             if str(book.img.dressid) == id:  # Convert id to string for comparison
    #                 print("hi", book.img.dressid, id)
    #                 book.delete()

    #     total = 0

    #     # Recalculate total after deleting the dress
    #     for dress in dresses:
    #         if dress.img and dress.img.price is not None:
    #             total += int(dress.img.price)
    #             print(total)
    #             dress.total = total
    #             dress.save()

    #     # Delete dresses with Booked_at more than 30 days old
    #     current_date = timezone.now()
    #     dresses.filter(Booked_at__lt=current_date - timezone.timedelta(days=30)).delete()

    #     # Filter booked dresses again after deletion
    #     dresses = booked.objects.filter(email=email)

    #     context = {'bookings': dresses, 'total': total}
    #     print(context)
    #     return render(request, 'bookedview.html', context)
    
    #payment block
    #cliend id for client side integration
    #security key for server side integration
    elif 'b2' in k:
            price=request.POST.get('price')
            email=request.POST.get('email')
            print(email,price)
            # user1=User.objects.get(username=email)
            # user1.quantity-=1
            # user1.save()
            # user=booked.objects.get(email=email)
            # print(type(user.total))
            # total=user.total
            # total-=int(price)
            # print(total)
            # user.total=total
            # user.save()
            return render(request,'pay.html',{'price':price,'email':email})
        
    return render(request,'bookedview.html')

# import os
# import paypalrestsdk
# from django.conf import settings
# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.decorators import api_view

# # Configure PayPal SDK
# paypalrestsdk.configure({
#     "mode": settings.PAYPAL_MODE,  
#     "client_id": settings.PAYPAL_CLIENT_ID,
#     "client_secret": settings.PAYPAL_CLIENT_SECRET,
# })

# @api_view(["POST"])
# def create_order(request):
#     """Create a PayPal order."""
#     data = request.data
#     cart = data.get("cart", [])

#     if not cart:
#         return JsonResponse({"error": "Cart is empty"}, status=400)

#     total = sum(item["price"] * item["quantity"] for item in cart)

#     payment = paypalrestsdk.Payment({
#         "intent": "sale",
#         "payer": {"payment_method": "paypal"},
#         "transactions": [{
#             "amount": {"total": f"{total:.2f}", "currency": "USD"},
#             "item_list": {"items": [
#                 {
#                     "name": item["name"],
#                     "sku": item.get("sku", ""),
#                     "price": f"{item['price']:.2f}",
#                     "currency": "USD",
#                     "quantity": item["quantity"]
#                 } for item in cart
#             ]}
#         }],
#         "redirect_urls": {
#             "return_url": settings.PAYPAL_RETURN_URL,
#             "cancel_url": settings.PAYPAL_CANCEL_URL
#         }
#     })

#     if payment.create():
#         return JsonResponse({"id": payment.id, "approval_url": payment.links[1].href})
#     else:
#         return JsonResponse({"error": payment.error}, status=400)


# @api_view(["POST"])
# def capture_order(request, order_id):
#     """Capture payment for a PayPal order."""
#     payment = paypalrestsdk.Payment.find(order_id)

#     if payment.execute({"payer_id": request.data.get("payer_id")}):
#         return JsonResponse({"message": "Payment successful", "payment": payment.to_dict()})
#     else:
#         return JsonResponse({"error": payment.error}, status=400)


# def payment_success(request):
#     return render(request, "paymentsuccess.html")


# def payment_cancel(request):
#     return render(request, "paymentcancel.html")
 
 
 
 
 
 
 
 
 
 
 
# def pay(request):
#     if request.method=="POST":
#         price=request.POST.get('price')
#         email=request.POST.get('email')
#         user1=User.objects.get(username=email)
#         user1.quantity-=1
#         user1.save()
#         user=booked.objects.get(email=email)
#         print(type(user.total))
#         total=int(user.total)
#         total-=int(price)
#         print(total)
#         user.total=total
#         user.status="Paid"
#         messages.success(request,f"you Paid {price}")
#         user.save()
#     return render(request,'pay.html')  
# # import random 
# # def otp(request):
# #     if request.method=="POST":
# #         email=request.POST.get("email")
# #         email1=User.objects.filter(email_id=email).first()
# #         if email1 is None:
# #             otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
# #             subject='OTP for application'
# #             message=f'Hi ,your otp is {otp}'
# #             email_from= settings.EMAIL_HOST_USER
# #             recipeient_list=[email]
# #             send_mail(subject,message,email_from,recipeient_list)
# #             messages.success(request,"Email sent")
# #             return render(request, 'otp.html', {'otp': otp})
# #         else:
# #             messages.success(request,"You already applied..:)")
# #             return render(request,"register.html")
        
# # def checkotp1(request):
# #     if request.method=="POST":
# #         gotp=request.POST.get("gotp")
# #         email=request.POST.get("email")
# #         otp = request.POST.get("otp")
# #         print(gotp,email,otp)
# #         if otp==gotp:
# #             return render(request,"bookedview.html")
# #         else:
# #             messages.success(request,"OTP does not match..?")
# #             return render(request,'otp1.html')
# def superview(request):
#     print("hi")
#     if request.method=="POST":
#         k=request.POST.get('btn',"")  
#         if 'booked' in k:
#             book=booked.objects.all()
#             context={'booked_dresses':book}
#             return render(request,'allbookeddress.html',context)
#         elif 'loggedview' in k:
#             user=profile.objects.all()
#             context={'profiles':user}
#             return render(request,"userprofiles.html",context)
#         else:
#             messages.success(request,'Something went wrong!Please Retry')
#         return render(request,'superuser.html')
    
    
    
    
# # from django.shortcuts import render, redirect
# # from paypal.standard.forms import PayPalPaymentsForm
# # from django.conf import settings

# # def payment(request):
# #     paypal_dict = {
# #         "business": settings.PAYPAL_RECEIVER_EMAIL,
# #         "amount": "10.00",  # Example amount
# #         "item_name": "Dress Purchase",
# #         "invoice": "12345",  # Unique invoice ID
# #         "currency_code": "USD",
# #         "notify_url": request.build_absolute_uri("/paypal/"),
# #         "return_url": request.build_absolute_uri("/payment-success/"),
# #         "cancel_return": request.build_absolute_uri("/payment-cancel/"),
# #     }

# #     form = PayPalPaymentsForm(initial=paypal_dict)
# #     return render(request, "payment.html", {"form": form})

# # def payment_success(request):
# #     return render(request, "success.html")

# # def payment_cancel(request):
# #     return render(request, "cancel.html")



# from django.shortcuts import render
# from paypal.standard.forms import PayPalPaymentsForm
# from django.conf import settings

# def test_payment(request):
#     paypal_dict = {
#         "business": settings.PAYPAL_CLIENT_ID,
#         "amount": "10.00",
#         "item_name": "Test Dress",
#         "invoice": "TEST12345",
#         "currency_code": "USD",
#         "notify_url": request.build_absolute_uri("/paypal-ipn/"),
#         "return_url": request.build_absolute_uri("/payment-success/"),
#         "cancel_return": request.build_absolute_uri("/payment-cancel/"),
#     }

#     form = PayPalPaymentsForm(initial=paypal_dict)
#     return render(request, "payment.html", {"form": form})
