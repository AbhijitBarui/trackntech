from django.shortcuts import render, redirect
from .models import Interest
from django.contrib import messages

def interest(request):
    if request.method == 'POST':
        print(request.POST)
        content_id = request.POST['content_id']
        content = request.POST['content']
        name = request.POST['name']
        topic = request.POST['topic']
        user_id = request.POST['user_id']
        author_email = request.POST['author_email']

        #Duplicacy check
        if request.user.is_authenticated:
            user_id=request.user.id
            is_interested = Interest.objects.all().filter(content_id=content_id, user_id=user_id)
            if is_interested:
                messages.error(request, 'This blog is already in your favorites')
                return redirect('/contents/'+content_id)
        
        interest = Interest(content=content, content_id=content_id, name=name, topic=topic, user_id=user_id)

        interest.save()

        messages.success(request, 'Blog is added to your favorites')
        return redirect('/contents/'+content_id)