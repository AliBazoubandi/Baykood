from django.shortcuts import render, get_object_or_404
from .models import Post, Tag
from django.core.paginator import Paginator


def post_list(request, tag_slug=None):
    posts   = Post.objects.filter(is_published=True)
    tags    = Tag.objects.all()
    current_tag = None

    if tag_slug:
        current_tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags=current_tag)

    paginator = Paginator(posts, 6)  # 6 posts per page
    page      = request.GET.get('page')
    page_obj  = paginator.get_page(page)

    return render(request, 'blog/post_list.html', {
        'page_obj':    page_obj,
        'posts':       page_obj,
        'tags':        tags,
        'current_tag': current_tag,
    })


def post_detail(request, slug):
    post         = get_object_or_404(Post, slug=slug, is_published=True)
    related      = Post.objects.filter(
        tags__in=post.tags.all(), is_published=True
    ).exclude(id=post.id).distinct()[:3]
    embed_url    = post.get_embed_url()

    return render(request, 'blog/post_detail.html', {
        'post':      post,
        'related':   related,
        'embed_url': embed_url,
    })