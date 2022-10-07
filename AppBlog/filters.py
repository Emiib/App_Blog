import django_filters
from django_filters import ChoiceFilter
from .models import Post


STATUS_CHOICES = [
                ('Action', 'Action'),('Adventure', 'Adventure'),
                ('Science Fiction', 'Science Fiction'), ('Sports', 'Sports'),
                ('Thriller', 'Thriller'), ('Shounen', 'Shounen'),('Fantasy', 'Fantasy')
                ]


class PostFilter(django_filters.FilterSet):
    category = ChoiceFilter(choices=STATUS_CHOICES)

    class Meta:
        model = Post
        fields = ['category']