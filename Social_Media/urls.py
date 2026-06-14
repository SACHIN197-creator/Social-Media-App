"""
URL configuration for Social_Media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from testapp import views as tv
from postapp import views as pv

urlpatterns = [

    path('admin/',admin.site.urls),

    path('',tv.login_view,name='login'),

    path('register/',tv.register,name='register'),

    path('logout/',tv.logout_view,name='logout'),

    path('home/',pv.home,name='home'),

    path('create-post/',pv.create_post,name='create_post'),

    path('like/<int:id>/',pv.like_post,name='like'),

    path('comment/<int:id>/',pv.comment_post,name='comment'),

    path('delete/<int:id>/',pv.delete_post,name='delete'),

    path('profile/<int:id>/',tv.profile,name='profile'),

    path('edit-profile/',tv.edit_profile,name='edit_profile'),

    path('follow/<int:id>/',tv.follow_user,name='follow'),

    path('search/',tv.search_user,name='search'),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)