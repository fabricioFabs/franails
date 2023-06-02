from django.shortcuts import render
from django.http import HttpResponse
from post .models import Post
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def inicio(request):
    return render(request,'paginas/homebase.html')
    
def post_list(request):
    template_name = 'paginas/post-list.html'
    post = Post.objects.all()
    context = {
        'post':post
        }
    return render(request, template_name, context)

def post_detail(request, id):
    template_name = 'post-detail.html'
    post = Posts.objects.get(id=id)
    print(post)
    context = {
        'post': post
    }
    return render(request, template_name, context)

def post_create(request):
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

            messages.success(request, 'O post foi criado com sucesso')
            return HttpResponseRedirect(reverse('post-list'))

    form = PostsForm()
    return render(request, 'post-form.html', {"form": form})


def post_delete(request, id):
    post=Posts.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'post deletado com sucesso')
        return HttpResponseRedirect(reverse('post-list'))
    return render(request, 'post-delete.html')
