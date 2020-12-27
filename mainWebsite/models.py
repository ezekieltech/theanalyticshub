from django.db import models
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

User = settings.AUTH_USER_MODEL


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

STAGE = (
    ('Planning', "Planning"),
    ('Execution', "Execution"),
    ('Optimization', "Optimization")
)

TYPE = (
    ('post', "post"),
    ('page', "page"),
    ('case_studies', "case_studies"),
    ('featured','featured'),
    ('staff', 'staff'),
    ('project', 'project')
)

class Service (models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='service/', blank=True, null=True)
    sales_point = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    post_image = models.ImageField(
        upload_to='post/', default='img/post/personal.png')
    post_image_alt = models.CharField(max_length=200, blank=True,
                                      null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                   related_name='service_post', blank=True,
                                   null=True,)
    # industry = models.ForeignKey('Industry', on_delete=models.CASCADE, null = True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    focus = RichTextField(blank=True,null=True)
    content = RichTextUploadingField (blank=True,null=True,default='Post Content')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    stage = models.CharField(max_length=400, choices=STAGE, blank=True,
                             null=True)
    post_type = models.CharField(max_length=400, choices=TYPE,  blank=True,
                             null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Industry (models.Model):
    pass
    # name = models.CharField(max_length=200, unique=True)
    # focus = models.TextField()

    # class Meta:
    #     ordering = ['name']

    # def __str__(self):
    #     return self.name
    



