from unicodedata import category
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# CBV - se utiliza solamente para la vista borrar post + decorador
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

#decorador para funciones - (condicionante de estar logueado)
from django.contrib.auth.decorators import login_required

####convierte los modelos en diccionarios, manteniendo los campos intactos.
from django.forms.models import model_to_dict
#para respuestas basadas en diccionarios
from django.http import JsonResponse

from AppProfile.views import defaultAvatar

##### importamos modelos y formularios a utilizar
from .models import Post
from .forms import NewPost, CommentForm
from AppProfile.models import Avatar

from .filters import ChoiceFilter



###### Vista de inicio extendida desde padre.html
def inicio(request):
    return render(request, 'inicio.html')


##### En esta funcion vamos a poder ver todos los posts. 
def posts(request):
    
    posts = Post.objects.all()
    posts = Post.objects.order_by('-created_at')

    return render(request, 'pages.html', {'posts': posts})


##### funcion para agregar un nuevo articulo 
@login_required
def add_post(request):
    if request.method != 'POST':
        form = NewPost()
        return render(request, "new_post.html", {"form":form, "avatar":defaultAvatar(request)})
    else:
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            posts = Post.objects.all()
            return redirect('posts')

    context = {'form': form, 'posts': posts, 'title': 'New Post'}
    return render(request, 'new_post.html', context)

####### Funcion para editar los articulos. (necesario estar logueado)
@login_required
def edit_post(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        form = NewPost(instance=post)
    else:
        form = NewPost(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            posts = Post.objects.all()
            return redirect('posts')
    return render(request, 'editpost.html',{'post':post, 'form': form})

##### funcion para poder ver un post estando con una sesion activa. 
@login_required
def post_detail(request, post_id):
    
    post = Post.objects.get(id = post_id) 

    #context = {'Title': 'Detail', 'subtitle': post.anime_name,  'posts': post}
    return render(request, 'post_detail.html',{'post':post})

##### probamos VBC
######### En este caso para eliminar un articulo ya publicado.
class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy(posts)
    

###### Funcion para agregar comentarios al articulo.
def addComment(request):
    if request.method == 'POST':
        formComment = CommentForm(request.POST)
        if formComment.is_valid():
            instance = formComment.save(commit=False)
            instance.id = int(request.POST.get('post'))
            instance.save()
            return JsonResponse(model_to_dict(instance, fields=['name_person']), status=201)
        else:
            return JsonResponse(formComment.errors, safe=False, status=200)

##### FUNCION PARA LA VISTA DE "SOBRE NOSOTRSOS"
def about(request):
    return render(request, 'about.html')


def buscar(request):  #####VER ESTA FUNCION, SI ES NECESARIA! 
    if request.method == 'POST':
        posts = Post.objects.filter(content__contains=request.POST.get('filtro'))
        return render(request, 'busqueda.html', {'posts': posts})
    return redirect('inicio')

def category(request):
    category = Post.objects.all().order_by('-created_at')
    filter = ChoiceFilter(request.GET, queryset=category)
    category = filter.queryset
    context = {
        'category': category,
        'filter': filter,}
    return render(request, 'post_cat.html', context)