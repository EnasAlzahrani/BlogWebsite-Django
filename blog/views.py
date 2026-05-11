from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, Post, Comment, Category


def main(request):
 template = loader.get_template('main.html')
 return HttpResponse(template.render())

def users(request):
    myusers = User.objects.all()
    template = loader.get_template('users.html')
    context = {
       'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))

def blogs(request):
   myposts = Post.objects.all()
   template = loader.get_template('blogs.html')
   context = {
      'myposts': myposts,
   }
   return HttpResponse(template.render(context, request))

def comments(request):
   mycomments = Comment.objects.all()
   template = loader.get_template('comments.html')
   context = {
      'mycomments': mycomments,
   }
   return HttpResponse(template.render(context, request))

def categories(request):
   mycategories = Category.objects.all()
   template = loader.get_template('categories.html')
   context = {
      'mycategories': mycategories,
   }
   return HttpResponse(template.render(context, request))

def blogdetails(request, id):
   post = Post.objects.get(ID=id)
   template = loader.get_template('blogdetails.html')
   context = {
      'post': post,
   }
   return HttpResponse(template.render(context, request))




