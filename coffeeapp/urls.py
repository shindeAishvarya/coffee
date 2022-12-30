from django.urls import  path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about, name  = 'about'),
    path('contact',views.contact, name ='contact' ),
    path('menu', views.menu, name = 'menu'),
    path('service', views.service , name= 'service'),
    path('reservation', views.reservation , name= 'reservation'),
    path('testimonial' , views.testimonial , name= 'testimonial')


]
