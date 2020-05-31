from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.db.models import Q
from users.models import UserProfile



@login_required()
def books(request):
        context = {
            'posts': Post.objects.filter(category ='BOOKS')
        }

        return render(request, 'blog/books.html',context)


@login_required()
def labs(request):
    context= {
        'posts': Post.objects.filter(category='LAB ACCESSORIES').order_by('-date_posted')
    }
    return render(request, 'blog/books.html',context)



@login_required()
def electronics(request):
    context= {
        'posts': Post.objects.filter(category='ELECTRONICS').order_by('-date_posted')

    }
    return render(request, 'blog/books.html',context)



@login_required()
def others(request):
    context= {
        'posts': Post.objects.filter(category='OTHERS').order_by('-date_posted')
    }
    return render(request, 'blog/books.html',context)




class PostTemplateView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name= 'posts'
    ordering = ['-date_posted']
    



class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post






class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['Product_name','desc','price','category','Phone_number','Image']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user


        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['Product_name', 'desc', 'price', 'category','Image']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
           return True
        return False



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/sell'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
           return True
        return False



@login_required
def search(request):
    query = request.GET.get("search",None)
    qs = Post.objects.all()
    if query is not None:
        qs = qs.filter(
            Q(Product_name__icontains=query) |
            Q(desc__icontains=query)

        )
    context = {
        'posts': qs,
    }
    if len(qs)==0 or len(query)<4:
        return render (request,'blog/search_not_found.html')
    else   :
      return render(request, 'blog/home.html', context)