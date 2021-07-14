from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from content import forms
import content;
from content.models import BlogWrite
import uuid
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

def blog_list(request):
    blogs = BlogWrite.objects.all()
    return render(request, 'content_template/index.html', context={'blogs':blogs})

def my_blog(request):
    return render(request, 'content_template/my_blog.html', context={})


def blogRead(request,slug):
    read_blog = BlogWrite.objects.get(slug=slug)
    hit_count = HitCount.objects.get_for_object(read_blog)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    

    file_name = read_blog.title+"."+"doc"
    open_from = "media\\document\\"+file_name
    file = open(open_from,'r')
    full_blog = file.read()
    return render(request,'content_template/open_blog.html',context={'read_blog':read_blog, 'full_blog':full_blog})


def blogWrite(request):
    form = forms.BlogWriteForm()

    if request.method=='POST':
        form = forms.BlogWriteForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.author = request.user
            form_data.slug = form_data.title.replace(" ","-")+"-"+str(uuid.uuid4())
            main_content = form_data.blog_content
            form_data.blog_content = form_data.slug

            #save the blog content into a txt file to media folder
            
            file_name = form_data.title+"."+"doc"
            save_to = "media\\document\\"+file_name
            file = open(save_to,'a')
            file.write(main_content)
            file.close()
            form_data.save()
            return HttpResponseRedirect(reverse('content:blog_list'))
    return render(request,'content_template/blog_form.html',context={'form':form})



def blog_edit(request,slug):
    full_blog = BlogWrite.objects.get(slug=slug)

    file_name = full_blog.title+"."+"doc"
    open_from = "media\\document\\"+file_name
    file = open(open_from,'r')
    full_blog.blog_content = file.read()
    
    form = forms.BlogWriteForm(instance=full_blog)

    if request.method=='POST':
        form = forms.BlogWriteForm(request.POST, instance=full_blog)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.author = request.user
            form_data.slug = form_data.title.replace(" ","-")+"-"+str(uuid.uuid4())
            main_content = form_data.blog_content
            form_data.blog_content = form_data.slug

            #save the blog content into a txt file to media folder
            
            file_name = form_data.title+"."+"doc"
            save_to = "media\\document\\"+file_name
            file = open(save_to,'a')
            file.write(main_content)
            file.close()
            form_data.save()  
            return HttpResponseRedirect(reverse('content:my_blog'))
    return render(request,'content_template/blog_form.html', context={'form':form})

# Create your views here.
