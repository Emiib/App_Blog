from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


##### lista de opciones para guardar el articulo en un tipo de categoria de anime
STATUS_CHOICES = [
                ('Action', 'Action'),('Adventure', 'Adventure'),
                ('Fiction', 'Fiction'), ('Sports', 'Sports'),
                ('Thriller', 'Thriller'), ('Shounen', 'Shounen'),('Fantasy', 'Fantasy')
                ]

class Post(models.Model):

    anime_name = models.CharField(max_length=80, verbose_name='Título')
    sub_name = models.CharField(max_length=100, verbose_name='Subtitulo')
    content = RichTextField(max_length=5000, verbose_name='Contenido')
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateField(null=True, blank=True, verbose_name='Fecha de publicación')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Autor')
    photo = models.ImageField(upload_to='images/', default='images/no_image.jpg', null=True, verbose_name='Foto')
    category = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f'Autor: {self.user.username} -- Titulo: {self.anime_name} -- Contenido: {self.content[:(42 - (len(self.anime_name) - 4))]} -- Fecha de publicacion: {self.published_at}'

    class Meta:
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-published_at']

#### modelo para darle comentarios al articulo.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name_person = models.CharField(max_length=64, verbose_name='Nombre')
    content = models.TextField(max_length=100, verbose_name='Comentario')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario: {self.content} -- Autor:{self.name_person}'

    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at'] 