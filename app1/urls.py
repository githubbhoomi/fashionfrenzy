"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
path("",views.login,name="login"),
path("login",views.login,name="login"),
#  path("",views.home,name="home"),
 path("home",views.home,name="home"),
#  path("category/<str:type>/",views.category,name="category"),
     path("category/<str:category_type>/", views.category, name="category"),
#  path("men",views.men,name="men"),
#  path("women",views.women,name="women"),
#  path("kids",views.kids,name="kids"),-


    # path("traditional",views.traditional,name="traditional"),
    # path("kurtha",views.kurtha,name="kurtha"),
    # path("Partywear",views.Partywear,name="Partywear"),
    # path("Skirt",views.Skirt,name="Skirt"),
    # path("weddingwear",views.weddingwear,name="weddingwear"),
    path("registration",views.registration,name="registration"),
    
    path("image",views.image,name="image"),
    path("delete",views.delete1,name="delete1"),
    path("deletedress",views.deletedress,name="deletedress"),
    path("logout1",views.logout1,name="logout1"),
    path("changepass/<token>/",views.changepass,name="changepass"),
    path('messagelib',views.messagelib,name="messagelib"),
    path("forgotpass",views.forgotpass,name="forgotpass"),
    path("uprofile",views.uprofile,name="userprofiles"),
    path("view",views.view,name="view"),
    # path("register",views.register,name="register"),
    path("checkotp",views.checkotp,name="checkotp"),
    path("otp",views.otp,name="otp"),
    path("sendotp",views.sendotp,name="otp"),
    path("bookeddress",views.bookeddress,name="bookeddress"),
    path("bookedview",views.bookedview,name="bookedview"),
    path("booking",views.booking,name="booking"),
    path("profileedit",views.profileedit,name="profileedit"),
    path("mentypeofdress",views.mentypeofdress,name="men"),
    path("womentypeofdress",views.womentypeofdress,name="women"),
    path("kidstypeofdress",views.kidstypeofdress,name="kids"),
    path("sendingotp",views.sendingotp,name="sendingotp"),
    path("sendingotp",views.sendingotp,name="sendingotp"),
    path("cancelorpay",views.cancelorpay,name="cancelorpay"),
    # path("pay",views.pay,name="pay"),
    path("womens",views.womens,name="womens"),
    path("mens",views.mens,name="mens"),
    path("kid",views.kid,name="kid"),
    # path("superview",views.superview,name="superview"),
    
    #  path("success", views.payment_success, name="payment_success"),
    # path("cancel", views.payment_cancel, name="payment_cancel"),
    # path("api/orders", views.create_order, name="create_order"),
    # path("api/orders/<str:order_id>/capture", views.capture_order, name="capture_order"),
    
    # #   path('paypal/', include('paypal.standard.ipn.urls')),
    # # # path('payment/', views.payment, name='payment'),
    # # path('payment-success/', views.payment_success, name='payment_success'),
    # # path('payment-cancel/', views.payment_cancel, name='payment_cancel'),
    #  path('test-payment/', views.test_payment, name='test_payment'),
    

    # path('checkotp1',views.checkotp1,name="checkotp1"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
