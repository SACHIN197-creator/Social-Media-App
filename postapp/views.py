from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Post
from .models import Comment
from .models import Like


@login_required
def home(request):

    posts = Post.objects.all().order_by(
        '-created_at'
    )

    return render(
        request,
        'home.html',
        {'posts': posts}
    )


@login_required
def create_post(request):

    if request.method == "POST":

        content = request.POST.get(
            'content'
        )

        image = request.FILES.get(
            'image'
        )

        Post.objects.create(
            user=request.user,
            content=content,
            image=image
        )

    return redirect('home')


@login_required
def like_post(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )

    like = Like.objects.filter(
        user=request.user,
        post=post
    )

    if like.exists():

        like.delete()

    else:

        Like.objects.create(
            user=request.user,
            post=post
        )

    return redirect('home')


@login_required
def comment_post(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )

    if request.method == "POST":

        Comment.objects.create(
            post=post,
            user=request.user,
            text=request.POST['comment']
        )

    return redirect('home')


@login_required
def delete_post(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )

    if post.user == request.user:

        post.delete()

    return redirect('home')