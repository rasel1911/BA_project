
from .views import register, user_login, user_logout, home_views, Contact,Complete_user_data
from django.urls import include, path
urlpatterns = [
    
    path('', home_views, name='home'),
    
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact/', Contact, name='contact'),
    path('completeuser/', Complete_user_data, name='completeuser'),
]
