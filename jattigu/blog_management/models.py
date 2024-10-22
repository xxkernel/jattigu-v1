from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')

    # Дополнительные атрибуты
    description = models.TextField(blank=True, help_text="Описание категории блога")
    slug = models.SlugField(unique=True, help_text="Уникальный URL-слог для категории, используемый в URL")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Дата и время создания категории")
    updated_at = models.DateTimeField(auto_now=True, help_text="Дата и время последнего обновления категории")

    def get_all_subcategories(self):
        """Возвращает все подкатегории, связанные с данной категорией."""
        return self.subcategories.all()

    def has_subcategories(self):
        """Проверяет, есть ли у категории подкатегории."""
        return self.subcategories.exists()

    def __str__(self):
        return self.name




class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('BlogCategory', on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')

    # Дополнительные атрибуты
#   is_published = models.BooleanField(default=False, help_text="Флаг, указывающий, опубликован ли пост")
    published_at = models.DateTimeField(null=True, blank=True, help_text="Дата и время публикации поста")
#    tags = models.ManyToManyField('Tag', blank=True, related_name='blog_posts')

    def publish(self):
        """Опубликовать пост и установить дату публикации."""
        self.is_published = True
        self.published_at = models.DateTimeField.now()
        self.save()

    def unpublish(self):
        """Снять публикацию поста."""
        self.is_published = False
        self.published_at = None
        self.save()

    # def get_tags(self):
    #     """Возвращает список тегов, связанных с постом."""
    #     return self.tags.all()

    def __str__(self):
        return self.title


# class Tag(models.Model):
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
