from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Blog, Comments
from django.utils import timezone
from .forms import PostForm,BlogForm, CommentsForm
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comments.objects.filter(post=pk).order_by('created_date')
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.author = request.user
            comm.created_date = timezone.now()
            comm.post = Post.objects.filter(pk=pk)[0]
            comm.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentsForm()
    return render(request, 'blog/post_detail.html', {'post': post,'comments':comments})

def post_new(request, pk):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.blog = Blog.objects.filter(pk=pk)[0]
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def blog_list(request):
    blogs = Blog.objects.order_by('-created_date')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request,pk):
    blog = get_object_or_404(Blog, pk=pk)
    posts = Post.objects.filter(blog=pk).order_by('published_date')
    return render(request, 'blog/blog_detail.html', {'posts':posts,'blog':blog})

def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.BLOG, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.create_date = timezone.now()
            blog.save()
            return redirect('post_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_edit.html', {'form': form})

def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.created_date = timezone.now()
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
        return render(request, 'blog/blog_edit.html', {'form': form})

def add_comment(request, pk):
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.created_date = timezone.now()
            comment.post = Post.objects.filter(pk=pk)[0]
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentsForm()
        return render(request, 'blog/post_detail.html', {'form': form})


def comment_detail(request,pk):
    comment = get_object_or_404(Comments, pk=pk)
    post = comment.post
    return render(request, 'blog/comment_detail.html', {'comment':comment,'post_title':post.title})
