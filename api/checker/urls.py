from django.urls import path

from . import views

urlpatterns = [

    path('single_image/', views.single_image_prediction, name='single_image'),
]