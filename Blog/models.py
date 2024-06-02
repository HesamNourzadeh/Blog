from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html
class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title
class Post(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE  , verbose_name='نویسنده')
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100 , verbose_name='عنوان')
    body = models.TextField()
    image = models.ImageField(upload_to="image/Post")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=timezone.now())
    status = models.BooleanField(default=True , verbose_name='وضعیت')
    published = models.BooleanField(default=True , verbose_name='انتشار')
    slug = models.SlugField(blank=True , unique=True)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Post, self).save()
    def get_absolute_url(self):
        return reverse("detail:post" , args=[self.slug])

    def show_image(self):
        if self.image:
            return format_html(f'<img src = "{self.image.url}" width="60px" height="50px">')
        return format_html('<h2 style = "color : red">تصویر ندارد</h2>')
    show_image.short_description = 'نمایش عکس'
    def __str__(self):
        return f"{self.title} --- {self.body[:40]}"

class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    parent = models.ForeignKey('self' ,null=True,blank=True, on_delete=models.CASCADE , related_name='replied')
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


    def __str__(self):
        return self.body[:50]
class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='likes' , verbose_name='کاربر')
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='likes' , verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} --- {self.post.title}'

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
