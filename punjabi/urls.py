from django.urls import path
from . import views

urlpatterns=[
path('',views.index, name='home'),
path('hotel-in-ranchi',views.room, name='room'),
path('best-hotel-in-ranchi/<int:id>',views.roomview, name='roomview'),
path('contact', views.contact, name='contact'),
path('user-log', views.reg, name='reg'),
path('login', views.login, name='login'),
path('logout', views.logout, name='logout'),
path('booking', views.booking, name='booking'),
path('Restaurant-in-ranchi', views.restaurant, name='restaurant'),
path('review',views.review,name='review'),
path('select',views.select,name='select'),




]
