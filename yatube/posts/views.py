from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post, Group

NUMBER_POSTS = 10


def index(request):
    posts = Post.objects.select_related('author', 'group').only(
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
