from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Profile, Follow
from .forms import ProfileForm


def register(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            return render(
                request,
                'register.html',
                {'error': 'Username already exists'}
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Profile.objects.create(user=user)

        return redirect('login')

    return render(request, 'register.html')


def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('home')

        return render(
            request,
            'login.html',
            {'error': 'Invalid Credentials'}
        )

    return render(request, 'login.html')


def logout_view(request):

    logout(request)

    return redirect('login')


@login_required
def profile(request, id):

    profile_user = get_object_or_404(
        User,
        id=id
    )

    profile_obj = Profile.objects.get(
        user=profile_user
    )

    followers = Follow.objects.filter(
        following=profile_user
    ).count()

    following = Follow.objects.filter(
        follower=profile_user
    ).count()

    is_following = Follow.objects.filter(
        follower=request.user,
        following=profile_user
    ).exists()

    context = {
        'profile_user': profile_user,
        'profile_obj': profile_obj,
        'followers': followers,
        'following': following,
        'is_following': is_following,
    }

    return render(
        request,
        'profile.html',
        context
    )


@login_required
def edit_profile(request):

    profile = Profile.objects.get(
        user=request.user
    )

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect(
                'profile',
                request.user.id
            )

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        'edit_profile.html',
        {'form': form}
    )


@login_required
def follow_user(request, id):

    user_to_follow = User.objects.get(
        id=id
    )

    if user_to_follow != request.user:

        obj = Follow.objects.filter(
            follower=request.user,
            following=user_to_follow
        )

        if obj.exists():

            obj.delete()

        else:

            Follow.objects.create(
                follower=request.user,
                following=user_to_follow
            )

    return redirect(
        'profile',
        id
    )


@login_required
def search_user(request):

    query = request.GET.get(
        'q'
    )

    users = []

    if query:

        users = User.objects.filter(
            username__icontains=query
        )

    return render(
        request,
        'search.html',
        {'users': users}
    )