from django.urls import path
from .views import *

urlpatterns = [
    
    path('', inicio, name="inicio"),
    
    path('about/', about, name= "about"),
    path('buscar/', buscar,name= "buscar"),
    
    #    -----URL DE LOS POSTS ----- 
    path('posts/', posts, name= "posts"),
    path('add_post/', add_post, name="add_post"),
    path('edit_post/<post_id>/', edit_post, name="edit_post"),
    path('post_detail/<post_id>/', post_detail,name= "post_detail"),
    path('Post/DeletePost/<int:pk>', DeletePost.as_view(template_name='post_confirm_delete.html'), name='DeletePost'),

    #    -----URL DE LAS CATEGORIAS -----
    path('category/', category, name='category'),
    
    #    -----URL DE LOS COMENTARIOS ----- 
    path('addComment/', addComment, name= "addComment"),

    ]