from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .form import PostForm

# Create your views here.
def posts_create(request):
   
    form=PostForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
    context={
        'form':form,
        
    }
    return render(request,'post_form.html',context)

def posts_detail(request,id):
    details=get_object_or_404(Post,id=id)
    context={
       'details':details,
    }
    return render(request,'post_detail.html',context)

def posts_list(request):
    queryset=Post.objects.all()
    context={'title':'posts','objectlist':queryset,}
    return render(request,'index.html',context)

def posts_update(request):
    return HttpResponse("<h1>Hello! Updates</h1>")

def posts_delete(request):
    return HttpResponse("<h1>Hello! delete</h1>")