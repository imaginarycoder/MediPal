from django.conf.urls import url
from django.urls import path
from application import views

app_name = 'application'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('aboutPage/', views.aboutPage, name ='aboutPage'),
    path('contactPage/', views.contactPage, name ='contactPage'),
    path('diagnosis/', views.diagnosis, name = 'diagnosis'),
    path('doctors/', views.doctors, name = 'doctors'),
    path('meander/', views.meander, name = 'meander'),
    path('spiral/', views.spiral, name = 'spiral'),
    path('circle/', views.circle, name = 'circle'),
    path('gait/', views.gait, name = 'gait'),
    path('result_meander/', views.upload_meander, name = 'upload_meander'),
    path('result_spiral/', views.upload_spiral, name = 'upload_spiral'),
    path('result_circle/', views.upload_circle, name = 'upload_circle'),
    path('subscribers/', views.subscribers, name = 'subscribers'),
] 