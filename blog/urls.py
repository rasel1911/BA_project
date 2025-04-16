
from .views import Blog,Blog_details,chatbot_response,image_search_view
from django.urls import include, path
urlpatterns = [
    
    path('blog/', Blog, name='blog'),
    path('blogDetails/', Blog_details, name='blogDetails'),
    path('chatbot_response/', chatbot_response, name='chatbot_response'),
    path('image-search/', image_search_view, name='image_search'),
]
