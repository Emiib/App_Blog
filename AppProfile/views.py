from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views import View #ver

#formularios
from .forms import *
from django.contrib.auth.forms import AuthenticationForm

#modelos
from .models import *

#decoradores
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from axes.decorators import axes_dispatch
from django.views.decorators.csrf import csrf_exempt

#para login
from django.contrib.auth import login, authenticate

##### CRUD = Create   -  Read    -  Update              -   Delete
##### CRUD = register -  profile -  UpdateProfileView   -  deleteprofile

###### VISTA DE REGISTRO DE NUEVO USUARIO
def register(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data.get('username')
            formulario.save()
            return render(request, "inicio.html", {'username': username})
        else:
            return render(request, "signup.html", {"formulario":formulario})
    else:
        formulario=UserRegisterForm()
        return render(request, "signup.html", {"formulario":formulario})


###### VISTA CON DECORADORES DE AXES PARA QUE EL USUARIO SE LOGUEE Y MEDIDAS DE SEGURIDAD
@axes_dispatch
@csrf_exempt
def login_request(request):
    if request.method=="POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = request.POST["username"]
            passw = request.POST["password"]
            log_user=authenticate(request = request, username = username, password = passw)
            if log_user is not None:
                login(request, log_user)
                return render(request, 'inicio.html')
            else:
                return render(request, "login.html", {"formulario":formulario})
        else:
            return render(request, "login.html", {"formulario":formulario})  
    else:
        formulario=AuthenticationForm()
        return render(request, "login.html", {"formulario":formulario})


###### VISTA DEL PEFIL
@login_required
def profile(request):
    
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    user = request.user
    
    return render(request, 'profile.html',{"user":user, "avatar": avatar})


###### FUNCION PARA QUE SIENDO USUARIO PUEDA ACTUALIZAR SU PERFIL
@login_required
def UpdateProfile(request):

    user = request.user

    if request.method == "POST":

        form = UpdateProfileForm(instance=user, data=request.POST)

        if form.is_valid():
            user = form.save()  
            return render(request, "profile.html")

        else:
            return render(request, "update_profile.html", {"formulario":form, "user":user})
    else:
        form = UpdateProfileForm(instance=user)
        return render(request, "update_profile.html", {"formulario":form, "user":user})




@login_required
def UpdateProfileView(request):
    
    user = request.user

    if request.method != 'POST':
        form = UpdateProfileForm()

    else:
        # Data submitted. Formulario para guardar con los datos enviados por POST
        form = UpdateProfileForm(instance=user, data=request.POST)
        if form.is_valid():
            update_profile = form.save()
            login(request, update_profile, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('profile')
    return render(request, 'update_profile.html', {'form': form})








###### FUNCION PARA ELIMINAR PERFILES SIENDO SUPER USUARIO
###### Utilizo "lambda" (visto en la clase 25) para verificar que sea superusuario
@user_passes_test(lambda u: u.is_superuser)
@login_required
def deleteuser(request, id):
    user=User.objects.get(id=id)
    user.delete()
    user=User.objects.all()
    return render(request, "profile.html", {"user":user})





###### FUNCION PARA PODER ACTUALIZAR SU AVATAR ESTANDO LOGUEADO
#@user_passes_test(lambda u: u.is_superuser)
@login_required
def update_avatar(request):
    
    user = request.user

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method != 'POST':
        form = AvatarForm()
    
    else:
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            oldavatar = Avatar.objects.filter(user=request.user)

            if (len(oldavatar) > 0):
                new_avatar = oldavatar[0]
                new_avatar.avatar = form.cleaned_data['avatar']
                new_avatar.save()
            else:
                new_avatar = Avatar(user=user, avatar=form.cleaned_data['avatar'])
                new_avatar.save()
            return redirect(reverse('profile'))
    
    context = {'title': 'Update Avatar', 'subtitle': 'Update here',  'form': form, 'avatar': avatar}
    return render(request, 'update_avatar.html', context)


###### FUNCION PARA PONER QUE SE COLOQUE UN AVATAR PREDETERMINADO
def defaultAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)==0:
        avatar=lista[0].avatar.url
    else:
        avatar="/media/avatars/avatardefault.png"
    return avatar
