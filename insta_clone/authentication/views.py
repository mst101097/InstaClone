from django import forms
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from authentication.forms import UserForm

# Create your views here.


class SignUpView(View):
    template_name = 'authentication/signup.html'
    form_class = UserForm

    def get(self,request, *args, **kwargs):
        return render(request,self.template_name)

    def post(self,request, *args,**kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('form Save')
        
        context = {'form':form}

        return render(request,self.template_name,context)

class SignInView(View):
    template_name = 'authentication/signin.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        


        


        return render(request,self.template_name)
    





    


