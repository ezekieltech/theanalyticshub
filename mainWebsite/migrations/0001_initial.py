# Generated by Django 3.1.4 on 2020-12-20 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('post_image', models.ImageField(default='img/post/personal.png', upload_to='post/')),
                ('post_image_alt', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('focus', models.TextField(blank=True, null=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('stage', models.CharField(blank=True, choices=[('Planning', 'Planning'), ('Execution', 'Execution'), ('Optimization', 'Optimization')], max_length=400, null=True)),
                ('post_type', models.CharField(blank=True, choices=[('post', 'post'), ('page', 'page'), ('case_studies', 'case_studies'), ('featured', 'featured'), ('staff', 'staff'), ('project', 'project')], max_length=400, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]