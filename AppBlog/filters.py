import django_filters
from .models import Post


STATUS_CHOICES = [
                ('Action', 'Action'),('Adventure', 'Adventure'),
                ('Fiction', 'Fiction'), ('Sports', 'Sports'),
                ('Thriller', 'Thriller'), ('Shounen', 'Shounen'),('Fantasy', 'Fantasy')
                ]


class PostFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=STATUS_CHOICES)

    class Meta:
        model = Post
        fields = ['category']