from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# home function handles what the user will see when we want to send her home
# urls.py is where we'll map these views functions to handle those url patterns
#     when requested

# don't forget to point these to and load in our templates
def home(request):
    context = {
        'posts':Post.objects.all()
        }
    return render(request,
                  'blog/home.html',
                  context)

def about(request):
    return render(request,
                  'blog/about.html',
                  {'title': 'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'# the kind of template that the generic class-based view looks for: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class PostDetailView(DetailView):
    model = Post

# template for this is expected to be post_form.html
class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

    

