from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post, Group, User

NUMBER_POSTS = 10


def index(request):
    posts = Post.objects.prefetch_related('author', 'group').only(
        'text',
        'pub_date',
        'author__first_name',
        'author__last_name',
        'group__slug').order_by('-pub_date')
    paginator = Paginator(posts, NUMBER_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context=context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author').only(
        'text',
        'pub_date',
        'group_id',
        'author__first_name',
        'author__last_name').order_by('-pub_date')
    paginator = Paginator(posts, NUMBER_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'group': group
    }
    return render(request, 'posts/group_list.html', context=context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.prefetch_related('group').only(
        'text',
        'pub_date',
        'author__first_name',
        'author__last_name',
        'group__slug').order_by('-pub_date')
    paginator = Paginator(posts, NUMBER_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'author': author,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # post= get_object_or_404(Post, id=post_id)
    post = Post.objects.select_related('author', 'group').get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:profile', request.user)
    return render(request, 'posts/post_create.html', {'form': form})
