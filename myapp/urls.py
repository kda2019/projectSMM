from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('account/', account, name='account'),
    path('insta-content/<int:ig_id>', insta_content, name='insta-content'),
    path('get_creds/<int:user_id>', get_creds, name='get_creds'),
    path('local/redirect/local/redirect/', fb_auth, name='fb_auth'),
]
