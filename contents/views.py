from django.shortcuts import render, get_object_or_404
from .models import Content
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from itertools import chain

from taggit.models import Tag

from votes.models import Vote


def contents(request):
    contents = Content.objects.order_by('-content_date').filter(is_published=True)
    paginator = Paginator(contents, 3)
    page = request.GET.get('page')
    paged_contents = paginator.get_page(page)

    common_tags = Content.tags.most_common()[:4]
    context = {
        'contents': paged_contents,
        'common_tags': common_tags,
    }
    return render(request, 'contents/contents.html', context)

def content(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    up_count = len(Vote.objects.all().filter(content_id=content_id, has_upvoted = True))
    down_count = len(Vote.objects.all().filter(content_id=content_id, has_downvoted = True))
    context = {
        'content': content,
        'up_count': up_count,
        'down_count': down_count,
    }
    return render(request, 'contents/content.html', context)

def search(request):
    queryset_list = Content.objects.order_by('-content_date')
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list_0=queryset_list.filter(text_main__icontains=keywords)
            queryset_list_1=queryset_list.filter(text_1__icontains=keywords)
            queryset_list_2=queryset_list.filter(text_2__icontains=keywords)
            queryset_list_3=queryset_list.filter(text_3__icontains=keywords)
            queryset_list_4=queryset_list.filter(text_4__icontains=keywords)
            queryset_list_5=queryset_list.filter(text_5__icontains=keywords)
            queryset_list_6=queryset_list.filter(text_6__icontains=keywords)
            queryset_list_7=queryset_list.filter(text_7__icontains=keywords)
            queryset_list_8=queryset_list.filter(text_8__icontains=keywords)

            queryset_list= queryset_list_0 | queryset_list_1 | queryset_list_2 | queryset_list_3 | queryset_list_4 | queryset_list_5 | queryset_list_6 | queryset_list_7 | queryset_list_8
    context = {
        'contents': queryset_list,
        'values': request.GET
    }
    return render(request, 'contents/search.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Content.tags.most_common()[:4]
    contents = Content.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'contents':contents,
    }
    return render(request, 'contents/contents.html', context)
    