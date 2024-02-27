from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Post, Group

NUMBER_POSTS = 10


def index(request):
    posts = get_list_or_404(Post.objects.all().order_by('-pub_date')[:NUMBER_POSTS])
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context=context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:NUMBER_POSTS]
    context = {
        'posts': posts,
        'group': group
    }
    return render(request, 'posts/group_list.html', context=context)
