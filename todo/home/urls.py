from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,),
   path('add',views.add, name="add"),
   path('delete/<int:todo_id>',views.deleteItem, name="delete"),
]