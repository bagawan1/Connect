from django.urls import path
from . import views

appname = 'account'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/',views.logoutuser,name='logoutuser'),
    path('home/', views.home, name='home'),
    path('profile/',views.profile,name='profile'),
    path('entNews/',views.ent,name='ent'),
    path('sports/',views.sports,name='sports'),
    path('national/',views.national,name='national'),
]
