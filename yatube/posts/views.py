from django.shortcuts import render, get_object_or_404

from .models import Post, Group


# Create your views here.
def index(request):
    title = 'Последние обновления на сайте.'
    posts = Post.objects.all().order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context=context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)
    context = {
        'posts': posts,
        'group': group
    }
    return render(request, 'posts/group_list.html', context=context)
