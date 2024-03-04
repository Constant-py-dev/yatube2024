from django.shortcuts import render, get_object_or_404

from .models import Post, Group

NUMBER_POSTS = 10


def index(request):
    posts = Post.objects.select_related('author', 'group').only(
        'text',
        'pub_date',
        'author__first_name',
        'author__last_name',
        'group__slug').order_by('-pub_date')[:NUMBER_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context=context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author').only(
        'text',
        'pub_date',
        'group_id',
        'author__first_name',
        'author__last_name').order_by('-pub_date')[:NUMBER_POSTS]
    context = {
        'posts': posts,
        'group': group
    }
    return render(request, 'posts/group_list.html', context=context)
