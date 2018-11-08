from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from tinymce.models import HTMLField 

#Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published','Published'),
    )
    PAGE_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    )
    CHOICE1 = PAGE_CHOICES[0]
    CHOICE2 = PAGE_CHOICES[1]
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to ="blog-images",
                              null=True,
                              blank=True,
                              height_field="height_field",
                              width_field="width_field")
    height_field = models.PositiveIntegerField(default=640)
    width_field = models.PositiveIntegerField(default=640)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='blog_posts')
    body = HTMLField()
    page = models.CharField(max_length=2, choices=PAGE_CHOICES, default='1')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
