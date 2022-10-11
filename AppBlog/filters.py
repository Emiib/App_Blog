import django_filters
from django_filters import ChoiceFilter, CharFilter, DateTimeFromToRangeFilter
from .models import Post


STATUS_CHOICES = [
                ('Action', 'Action'),('Adventure', 'Adventure'),
                ('Fiction', 'Fiction'), ('Sports', 'Sports'),
                ('Thriller', 'Thriller'), ('Shounen', 'Shounen'),('Fantasy', 'Fantasy')
                ]
class PostFilter(django_filters.FilterSet):
    post = CharFilter(field_name = 'post',lookup_expr='icontains')
    category = ChoiceFilter(choices=STATUS_CHOICES)
    created_at = DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = ['category', 'post', 'created_at']