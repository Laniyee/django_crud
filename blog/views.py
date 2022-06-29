from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit  import DeleteView
# Create your views here.
class Post(ListView):
    model = Post
class Post(CreateView):
     model = Post
     fields = '__all__'
     success_url= reverse_lazy('blog:all')
class Post(DetailView):
    model= Post  
class Post(UpdateView):
     model = Post
     fields = '__all__'
     success_url= reverse_lazy('blog:all')
class Post(DeleteView):
     model = Post
     fields = '__all__'
     success_url= reverse_lazy('blog:all')         
