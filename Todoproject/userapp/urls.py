from django.urls import path
from.import views

app_name='app'
urlpatterns = [
    path('register/',views.registerUser ,name='register'),
    
    
]
