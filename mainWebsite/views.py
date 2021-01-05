from django.views import generic
from django.shortcuts import redirect
from .models import Post, Service, STAGE
from django_hosts.resolvers import reverse


class PostList(generic.ListView):
    template_name = 'mainWebsite/index.html'
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        list_of_case_studies = Post.objects.filter(status=1,post_type='featured').order_by('-created_on')
        list_of_services = Service.objects.all  # used for main and footer menu
        context['list_of_case_studies'] = list_of_case_studies[:5]
        for post in list_of_case_studies:
            print(post.post_image.url)
        context['list_of_services'] = list_of_services # used for main and footer menu
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'mainWebsite/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        related_blog_post_by_service = Post.objects.filter(status=1, post_type= self.object.post_type, service=self.object.service).order_by('-created_on').exclude(title=self.object.title)
        context['related_blog_post_by_service'] = related_blog_post_by_service[:5]
        list_of_services = Service.objects.all  # used for main and footer menu
        context['list_of_services'] = list_of_services # used for main and footer menu
        return context


class ServiceDetail(generic.DetailView):
    model = Service
    template_name = 'mainWebsite/service_details.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceDetail, self).get_context_data(**kwargs)
        list_of_services = Service.objects.all # used for main and footer menu
        context['list_of_services'] = list_of_services  # used for main and footer 
        list_of_post = Post.objects.filter(status=1).order_by('-created_on')[:3]
        context['list_of_post']  = list_of_post
        return context


class ServiceList(generic.ListView):
    model = Service
    template_name = 'service.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ServiceList, self).get_context_data(**kwargs)
        post_list = Post.objects.filter(status=1).order_by('-created_on')[:3]
        context['post_list'] = post_list
        list_of_services = Service.objects.all # used for main and footer menu
        context['list_of_services'] = list_of_services # used for main and footer menu
        return context
