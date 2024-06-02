import requests
from django.http import JsonResponse
from django.shortcuts import render, get_list_or_404, redirect
from .models import Post , Category,Comment,Message , Like
from django.core.paginator import Paginator
from .forms import ContactUsForm,MessageForm
from django.views.generic import FormView , DetailView , ListView
from django.urls import reverse_lazy
def post_detail(request , slug):
    post = Post.objects.get(slug = slug)
    if request.method == "POST":
        body = request.POST.get("message")
        parent_id = request.POST.get("parent_id")
        Comment.objects.create(body=body , post = post , user= request.user , parent_id = parent_id)
    if request.user.likes.filter(post__slug=slug , user_id=request.user.id).exists():
        is_like = True
    else:
        is_like = False
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.GET.get('action') == 'read_details':
        return JsonResponse({'body': post.body})

    return render(request , "Blog/post_detail.html" , {'post' : post , 'is_like' : is_like})
def post_list(request):
    post = Post.objects.filter(published = True)
    page_number = request.GET.get("page")
    paginator = Paginator(post , 1)
    objects_list = paginator.get_page(page_number)
    return render(request , 'Blog/post_list.html' , {'post' : objects_list})
def category_detail(request , pk=None):
    category = Category.objects.get(id=pk)
    posts = category.post_set.all()
    page_number = request.GET.get("page")
    paginator = Paginator(posts, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, 'Blog/search&category.html', {'post': objects_list})
def search(request):
    q  = request.GET.get('q')
    page_number = request.GET.get("page")
    post = Post.objects.filter(title__icontains=q)
    paginator = Paginator(post , 1)
    objects_list = paginator.get_page(page_number)
    return render(request , 'Blog/search&category.html' , {'post' : objects_list})
# def contactus(request):
#     if request.method == 'POST':
#         form = MessageForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = MessageForm()
#     return render(request , 'Blog/contact_us.html' , {'form' : form})

class PostListView(ListView):
    model = Post
    paginate_by = 2
    queryset = Post.objects.filter(published=True)
# class PostDetailView(DetailView):
#     model = Post

class ContactUsView(FormView):
    template_name = 'blog/contact_us.html'
    form_class = MessageForm
    success_url =reverse_lazy('home_app:homepage')
    def form_valid(self, form):
        form_data = form.cleaned_data
        Message.objects.create(**form_data)
        return super().form_valid(form)

def like(request , slug , pk):
    try:
        like = Like.objects.get(post__slug=slug , user_id=request.user.id)
        like.delete()
        return JsonResponse({"response" : "unliked"})
    except:
        Like.objects.create(post_id=pk , user_id= request.user.id)
        return JsonResponse({"response" : "liked"})
def aboutus(request):
    return render(request , 'Blog/aboutus.html' , {})
