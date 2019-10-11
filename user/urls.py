from django.urls import path
from . import views

urlpatterns=[
path('adminlogin',views.adminlogin, name='adminlogin'),
path('home',views.home, name='home'),
path('add-room', views.addroom, name='room'),
path('new-room', views.newroom, name='room'),
path('deletebooking/<int:rid>', views.deletebooking, name='deletebooking'),
path('confirm/<int:cid>', views.confirm, name='confirm'),
path('all-booking', views.allbooking, name='allbooking'),
path('gallery', views.gallery, name='gallery'),
path('new-gallery', views.new_gallery, name='new_gallery'),
path('show_restaurant',views.show_restaurant, name='show_restaurant'),
path('add_restaurant',views.add_restaurant, name='add_restaurant'),
path('delete_restaurant',views.delete_restaurant, name='delete_restaurant'),
path('show_contact',views.show_contact, name='show_contact'),
path('delete_room/<int:rmid>',views.delete_room, name='delete_room'),







]
