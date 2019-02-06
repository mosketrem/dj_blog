from django.shortcuts import render, get_object_or_404, redirect

from blog.models import PostRecord
from .forms import CreatePostForm


def index(request):
    return posts_list(request)


def posts_list(request):
    posts = PostRecord.objects.order_by('when_created')
    return render(request, 'blog/posts_list.html', {'posts': posts})


def view_post(request, slug):
    return render(request, 'blog/view_post.html', {
        'post': get_object_or_404(PostRecord, slug=slug)
    })


def create_post(request):
    if request.user.is_authenticated:
        # profile = User.objects.get(username=username)
        form = CreatePostForm()
        if request.method == 'POST':
            form = CreatePostForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('index')
        return render(request, 'blog/create.html', {'form': form})
    return redirect('index')


def edit_post(request, slug):
    post_record = get_object_or_404(PostRecord, slug=slug)
    if request.user.is_authenticated and request.user.username == post_record.author.username:
        form = CreatePostForm(instance=post_record)
        if request.method == 'POST':
            form = CreatePostForm(request.POST, instance=post_record)
            if form.is_valid():
                # instance = form.save(commit=False)
                # instance.author = request.user
                # instance.save()
                form.save()
                return redirect('view_blog_post', slug)
        return render(request, 'blog/create.html', {'form': form})
    return redirect('view_blog_post', slug)

