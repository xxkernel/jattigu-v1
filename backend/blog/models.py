# from django.db import models

# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     slug = models.SlugField(unique=True)
#     created_at = models.DateTimeField(auto_now_add=True, help_text="Дата и время создания категории")
#     updated_at = models.DateTimeField(auto_now=True, help_text="Дата и время последнего обновления категории")

#     def __str__(self):
#         return self.name
    

# class BlogPost(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     category = models.ForeignKey('BlogCategory', on_delete=models.SET_NULL, null=True, blank=True)
#     # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')

#     # Дополнительные атрибуты
# #   is_published = models.BooleanField(default=False, help_text="Флаг, указывающий, опубликован ли пост")
#     published_at = models.DateTimeField(null=True, blank=True, help_text="Дата и время публикации поста")
# #    tags = models.ManyToManyField('Tag', blank=True, related_name='blog_posts')

#     def publish(self):
#         """Опубликовать пост и установить дату публикации."""
#         self.is_published = True
#         self.published_at = models.DateTimeField.now()
#         self.save()

#     def unpublish(self):
#         """Снять публикацию поста."""
#         self.is_published = False
#         self.published_at = None
#         self.save()

#     # def get_tags(self):
#     #     """Возвращает список тегов, связанных с постом."""
#     #     return self.tags.all()

#     def __str__(self):
#         return self.title