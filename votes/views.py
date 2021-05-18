from django.shortcuts import redirect, render
from .models import Vote
from django.contrib import messages

def upvote(request):
    if request.method == 'POST':
        content_id = request.POST['content_id']
        content = request.POST['content']
        name = request.POST['name']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            has_object = Vote.objects.all().filter(content_id=content_id, user_id=user_id)
            is_upvoted = Vote.objects.all().filter(content_id=content_id, user_id=user_id, has_upvoted=True)
            is_downvoted = Vote.objects.all().filter(content_id=content_id, user_id=user_id, has_downvoted=True)
            if has_object:
                if is_downvoted:
                    is_downvoted.update(has_upvoted = True, has_downvoted = False)
                else:
                    if is_upvoted:
                        is_upvoted.update(has_upvoted = False)
                    else:
                        has_object.update(has_upvoted = True)
            else:
                has_upvoted = True

                vote = Vote(content=content, content_id=content_id, name=name, has_upvoted=has_upvoted, user_id=user_id)

                vote.save()
            messages.success(request,' your response is registered')
        else:
            messages.error(request, 'you need to log in first!')
        
        return redirect('/contents/'+content_id)

def downvote(request):
    if request.method == 'POST':
        content_id = request.POST['content_id']
        content = request.POST['content']
        name = request.POST['name']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            has_object = Vote.objects.all().filter(content_id=content_id, user_id=user_id)
            is_upvoted = Vote.objects.all().filter(content_id=content_id, user_id=user_id, has_upvoted=True)
            is_downvoted = Vote.objects.all().filter(content_id=content_id, user_id=user_id, has_downvoted=True)
            if has_object:
                if is_upvoted:
                    is_upvoted.update(has_downvoted = True, has_upvoted = False)
                else:
                    if is_downvoted:
                        is_downvoted.update(has_downvoted = False)
                    else:
                        has_object.update(has_downvoted = True)
            else:
                has_downvoted = True

                vote = Vote(content=content, content_id=content_id, name=name, has_downvoted=has_downvoted, user_id=user_id)

                vote.save()
            messages.success(request,' your response is registered')
        else:
            messages.error(request, 'you need to log in first!')
        
        return redirect('/contents/'+content_id)