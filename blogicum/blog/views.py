from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post
from django.utils import timezone

now = timezone.now()


def index(request):
    posts = (
        Post.objects
        .select_related('author', 'location', 'category')
        .filter(is_published=True,
                pub_date__lte=now,
                category__is_published=True)
        .order_by('-pub_date')[0:5]
    )
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        pk=post_id,
        pub_date__lte=now,
        is_published=True,
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True)
    posts = (
        Post.objects.filter(
            category=category,
            is_published=True,
            pub_date__lte=now)
        .order_by('-pub_date')
    )

    return render(request, 'blog/category.html',
                  {'category': category, 'post_list': posts})
