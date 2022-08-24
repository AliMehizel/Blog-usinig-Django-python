from http.client import HTTPResponse
from winreg import DeleteValue
from django.shortcuts import render,redirect
from .forms import  SignupForm, LoginForm
from django.views.generic import TemplateView,View,CreateView,DeleteView, UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate,logout
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
# Create your views here.


class BaseView(TemplateView):
    template_name = 'base.html'
    
    def get(self,request, *args, **kwrgs):
        posts = {'posts': Post.objects.all(), 'comment': Comment.objects.all()}
        return render(request, self.template_name, posts)
    
    
class HomeView(TemplateView,LoginRequiredMixin):
    template_name = 'home.html'
    context_object_name = 'post'
    def get(self,request, *args, **kwrgs):
        posts = {'posts': Post.objects.filter(auth=request.user)}
        return render(request, self.template_name, posts )
    
    
    
    
class LoginView(View):
    form_class = LoginForm
    template_name = 'login.html'
    context_object_name = 'post'
    def get(self, request):
        form = {'form': self.form_class}
        return render(request, self.template_name, form)
    
    def post(self,request):
        request_form = self.form_class(request.POST)
        
        
        if request_form.is_valid():
            auth_user = authenticate(username = request_form.cleaned_data['username'], password = request_form.cleaned_data['password'])
            
            if auth_user is not None:
                login(request, auth_user)
                return redirect('/home/')
            else:
                return redirect('/login/')
            
            
            
class SignupView(View):
    form_class = SignupForm
    template_name = 'signup.html'
    
    def get(self, request):
        form = {'form': self.form_class}
        return render(request, self.template_name, form)
    
    def post(self,request):
        request_form = self.form_class(request.POST)
        
        
        if request_form.is_valid():
            user = request_form.save()
            login(request, user)
            return redirect('/home/')
        else:
            
            return redirect('/signup/')
            
class LogoutView(View):
    def get(self,request):
        logout(request) 
        return redirect('/login/')
    
    

class PostCreate(CreateView,LoginRequiredMixin):
    model = Post
    template_name = 'createpost.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.auth = self.request.user
        return super(PostCreate, self).form_valid(form)
    
    



class PostUpdate(UpdateView,LoginRequiredMixin):
    model = Post
    template_name = 'postupdate.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('home')
    
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(auth=owner)



class PostDelete(DeleteView,LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'postdelete.html'
    
    
def PostDetail(request, pk):
    template = loader.get_template('postdetail.html')
    posts = Post.objects.filter(pk= pk)

    comment = Comment.objects.all()
    object = {
        'posts': posts, 
        'comment': comment,
        }
    if request.user.is_authenticated:
        if request.method == 'POST':
        
            commenttext = request.POST['comment']
            new_comment = Comment.objects.create(user=request.user,commentText=commenttext)
            new_comment.save()
            return redirect('base')
    else:
        return redirect('login')

    return HttpResponse(template.render(object, request))
        
        
    

    