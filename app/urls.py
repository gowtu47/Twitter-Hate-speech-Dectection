from django.urls import path
from.import views

urlpatterns=[
    path('',views.login_page),
    path('login/', views.login_page, name='login'),
     
    path('home_page',views.home_page),
   
    path('register_page',views.register_page),
    path('output',views.output),

]