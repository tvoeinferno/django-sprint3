from django.shortcuts import get_object_or_404, render

from django.utils import timezone

from blog.models import Category, Post

from core.constants import POSTS_ON_MAIN


def get_posts(queryset):
    now = timezone.now()
    return queryset.select_related(
        'author', 'location', 'category'
    ).filter(
        is_published=True,
        pub_date__lte=now,
        category__is_published=True
    )


def index(request):
    posts = get_posts(Post.objects)[:POSTS_ON_MAIN]
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, post_id):
    post = get_object_or_404(
        get_posts(Post.objects),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    posts = get_posts(category.posts.all())[:POSTS_ON_MAIN]
    return render(request, 'blog/category.html',
                  {'category': category, 'post_list': posts})
