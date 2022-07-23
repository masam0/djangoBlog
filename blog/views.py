from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag

# Create your views here.

tags = Tag.objects.all()
years = Post.objects.dates('date_published', 'year')
context = {
  "tags": tags,
  "years": years,
}

def index(request):
  latest_posts = Post.objects.order_by('-date_published')[:5]
  context["latest_posts"] = latest_posts
  return render(request, 'blog/index.html', context)

def article(request, slug):
  article = get_object_or_404(Post, slug=slug)
  context["article"] = article
  return render(request, 'blog/article.html', context)
