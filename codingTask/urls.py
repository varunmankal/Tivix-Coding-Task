"""codingTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from blog.views import home, newpost, detailpost, post_edit, signin

urlpatterns = [
    path('admin/', admin.site.urls),
	path('home/',  home, name="home"), # home page, where it lists all the existing posts
    path('',signin,name="signin"), # sign in page to enter username and password
	path('create/',newpost, name="newpost"), # it will take to a new page to create a post
	path('post/<int:pk>/',detailpost,name="detailpost"), # it displays full details of the desired post
    path('post/<int:pk>/edit/', post_edit, name='post_edit'), # it enables to edit the post
]
