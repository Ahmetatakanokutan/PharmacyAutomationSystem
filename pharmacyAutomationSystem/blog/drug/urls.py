from django.contrib import admin
from django.urls import path
from . import views


app_name = "drug"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('adddrug/',views.addDrug,name="adddrug"),
    path('drug/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.updateDrug,name="update"),
    path('delete/<int:id>',views.deleteDrug,name="delete"),
    path('',views.drugs,name="drugs"),
]
