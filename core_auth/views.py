from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import authenticate

import logging

logger = logging.getLogger('main')


class AuthLogin(View):
    def post(self, *args, **kwargs):
        form_values = self.request.POST

        user = authenticate(
            username=form_values.get('username_inp'), 
            password=form_values.get('password_inp')
        )

        logger.warning(user.get_username)

        if user is not None:            
            return redirect('entry')

        return redirect('login')
