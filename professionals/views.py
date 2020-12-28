from django.shortcuts import render
from django.views import generic
from django.conf import settings

from django_hosts.resolvers import reverse_host

from account.models import CustomUser 
from mainWebsite.models import Post, Service

from utilities.getUsernameFromSubdomain import getUsernameFromSubdomain

host = getUsernameFromSubdomain()

class UserDetail(generic.ListView):
    model = CustomUser
    template_name = 'professionals/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        account = CustomUser.objects.get(username=host)
        context['account'] = account
        return context


class UserPosts(generic.ListView):
    model = Post
    template_name = 'professionals/blog.html'

    def get_context_data(self, **kwargs):
        context = super(UserPosts, self).get_context_data(**kwargs)
        account = CustomUser.objects.get(username=host)
        context['account'] = account
        user_posts = Post.objects.filter(author__username=host)
        context['user_posts'] = user_posts
        all_projects = Post.objects.filter(author__username=host, post_type='project')
        context['all_projects'] = all_projects
        return context


class UserPostDetail(generic.DetailView):
    model = Post
    template_name = 'professionals/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserPostDetail, self).get_context_data(**kwargs)
        account = CustomUser.objects.get(username=host)
        context['account'] = account
        related_blog_post_by_service = Post.objects.filter(status=1, post_type= self.object.post_type, service=self.object.service).order_by('-created_on').exclude(title=self.object.title)
        context['related_blog_post_by_service'] = related_blog_post_by_service[:5]
        list_of_services = Service.objects.all  # used for main and footer menu
        context['list_of_services'] = list_of_services # used for main and footer menu
        return context
