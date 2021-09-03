from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic import View

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

import logging

logger = logging.getLogger('main')


class AuthLogin(View):
    def post(self, *args, **kwargs):
        form_values = self.request.POST
        
        user = authenticate(
            username=form_values.get('username_inp'), 
            password=form_values.get('pass_inp')
        )
          
        if user is not None:            
            return redirect('entry')

        return redirect('login')


class AuthRegister(View):
    def post(self, *args, **kwargs):
        form_values = self.request.POST
        
        try:
            user = User.objects.create_user(
                username=form_values.get('username_inp'), 
                email=form_values.get('email_inp'), 
                password=form_values.get('pass_inp')
            )
          
        except Exception as err:
            logger.warning(f"create user error: {err}")
            return redirect('register')

        if user is not None:            
            return redirect('login') 

        return redirect('register')