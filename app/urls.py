from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.loginPage, name='login'),
    path('<int:pk>/', views.edit_intent, name='edit'),
    path('delete/<int:pk>/', views.delete_intent, name='delete'),
    path('logout',views.logoutPage , name='logout'),
    path('register', views.registerPage, name='register'),
    path('chatbot', views.chatbotPage, name='chatbot'),


]
