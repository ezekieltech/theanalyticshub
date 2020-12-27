from django.shortcuts import render
from django.views import generic
from django.conf import settings

from django_hosts.resolvers import reverse_host

from account.models import CustomUser 
from mainWebsite.models import Post, Service

# Create your views here.
User = settings.AUTH_USER_MODEL

class UserDetail(generic.ListView):
    model = CustomUser
    template_name = 'professionals/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        return context

class UserPosts(generic.ListView):
    model = Post
    template_name = 'professionals/blog.html'

    def get_context_data(self, **kwargs):
        context = super(UserPosts, self).get_context_data(**kwargs)
        host = reverse_host('user-area', args=('ezekiel',))
        host = host.split('.')[0]
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
        # related_blog_post_by_service = Post.objects.filter(status=1, post_type= self.object.post_type, service=self.object.service).order_by('-created_on').exclude(title=self.object.title)
        # context['related_blog_post_by_service'] = related_blog_post_by_service[:5]
        list_of_services = Service.objects.all  # used for main and footer menu
        context['list_of_services'] = list_of_services # used for main and footer menu
        return context

def get_post(request, user):
    context = {}
    print(user)
    user = CustomUser.objects.get(username=user)
    print (user)
    all_post = Post.objects.filter(author=user)
    all_projects = Post.objects.filter(author=user, post_type='project')
    context['all_post'] = all_post
    context['all_projects'] = all_projects
    context['pk'] = user.id
    return render(request, 'professionals/blog.html', context)
    