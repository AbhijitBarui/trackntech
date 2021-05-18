from django.shortcuts import render, redirect
from .models import Follow
from django.contrib import messages

from django.core.mail import send_mail

def follow(request):
    if request.method == 'POST':
        content_id = request.POST['content_id']
        author_id = request.POST['author_id']
        name = request.POST['name']
        user_id = request.POST['user_id']
        email = request.POST['email']
        phone = request.POST['phone']
        author_email = request.POST['author_email']

        #Duplicacy check
        if request.user.is_authenticated:
            user_id=request.user.id
            is_followed = Follow.objects.all().filter(author_id=author_id, user_id=user_id)
            if is_followed:
                messages.error(request, 'you are already suscribed to this author')
                return redirect('/contents/'+content_id)
        
        follow = Follow(author_id=author_id, name=name, user_id=user_id, email=email, phone=phone)

        follow.save()

        #send_mail
        send_mail(
            'sub: New Follower',
            'Congrats! you got a new follower, ' + name + '. Log into for more info',
            'trackandtech1@gmail.com',
            [author_email],
            fail_silently=False,
        )
        send_mail(
            'sub: Follow Request Successful',
            '''Congrats! your follow request is processed. Update from your favorite author will reach to you in no time!
            Thank you for staying connected!!''',
            'trackandtech1@gmail.com',
            [email,],
            fail_silently=False,
        )

        messages.success(request, 'Subscribed successfully! Updates will be sent on provided mail regularly.')
        return redirect('/contents/'+content_id)