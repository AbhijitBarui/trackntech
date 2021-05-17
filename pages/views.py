from django.shortcuts import render
from contents.models import Content
from authors.models import Author

def index(request):
    contents = Content.objects.order_by('-content_date').filter(is_published=True)[:3]
    context = {
        'contents': contents
    }
    return render(request, 'pages/index.html', context)

def about(request):
    authors = Author.objects.order_by('-hire_date')
    mvp_authors = Author.objects.all().filter(is_mvp=True)
    context = {
        'authors': authors,
        'mvp_authors': mvp_authors
    }
    return render(request, 'pages/about.html', context)