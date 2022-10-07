from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('register/', register, name="register"),
    path('login/', login_request, name="login"),
    path('profile/', profile, name="profile"),
    path('updateprofile/', UpdateProfileView, name='updateprofile' ),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('updateavatar/', update_avatar, name="updateavatar"),

]   