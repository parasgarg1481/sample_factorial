from django.urls import path
from . import views
#urlconf module 
urlpatterns = [
    path('',views.sayHello,name='sayHello'),
    path('factorial',views.fact,name='fact')
]